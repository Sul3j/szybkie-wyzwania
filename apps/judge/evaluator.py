
# Code evaluator that runs user code in Docker sandbox.

import json
import time
import docker
from django.conf import settings


class CodeEvaluator:
    """Evaluates code submissions in isolated Docker containers."""

    def __init__(self, submission):
        """
        Initialize evaluator with submission.

        Args:
            submission: Submission instance to evaluate
        """
        self.submission = submission
        self.problem = submission.problem
        self.language = submission.language
        self.code = submission.code
        # Use from_env() to work across different platforms (Linux, Windows/WSL, macOS)
        self.docker_client = docker.from_env()

    def evaluate(self):
        """
        Main evaluation method.

        Returns:
            dict: Evaluation results with status, test_results, etc.
        """
        try:
            # Get test cases
            test_cases = self.problem.test_cases.all().order_by('order')

            if not test_cases.exists():
                return {
                    'status': 'internal_error',
                    'error_message': 'No test cases found for this problem',
                    'test_results': []
                }

            # Run all test cases
            test_results = []
            total_execution_time = 0
            max_memory_used = 0

            for test_case in test_cases:
                result = self._run_test_case(test_case)
                test_results.append(result)

                # Track metrics
                if result.get('execution_time'):
                    total_execution_time += result['execution_time']
                if result.get('memory_used'):
                    max_memory_used = max(max_memory_used, result['memory_used'])

                # Stop on first failure (optional - can be changed)
                if not result.get('passed', False):
                    break

            # Determine overall status
            all_passed = all(r.get('passed', False) for r in test_results)
            status = 'accepted' if all_passed else self._determine_status(test_results)

            return {
                'status': status,
                'test_results': test_results,
                'execution_time': total_execution_time,
                'memory_used': max_memory_used,
                'error_message': self._get_error_message(test_results) if not all_passed else ''
            }

        except Exception as e:
            return {
                'status': 'internal_error',
                'error_message': f'Evaluation error: {str(e)}',
                'test_results': []
            }

    def _run_test_case(self, test_case):
        """
        Run a single test case in Docker container.

        Args:
            test_case: TestCase instance

        Returns:
            dict: Test case result
        """
        try:
            # Get Docker image for language
            docker_image = settings.SUPPORTED_LANGUAGES[self.language]['docker_image']

            # Prepare code and test data
            test_input = test_case.input_data
            expected_output = test_case.expected_output.strip()

            # Create complete executable code with wrapper
            executable_code = self._prepare_executable_code(test_input)

            # Create container
            container_name = f'code-train-sandbox-{self.submission.id}-{test_case.id}'

            # Prepare environment
            environment = {
                'TIME_LIMIT': str(self.problem.time_limit),
                'MEMORY_LIMIT': str(self.problem.memory_limit)
            }

            start_time = time.time()

            # Prepare command based on language
            if self.language == 'python':
                command = ['python', '-c', executable_code]
            elif self.language == 'javascript':
                command = ['node', '-e', executable_code]
            elif self.language == 'cpp':
                # For C++, compile first, then run
                import base64
                encoded_code = base64.b64encode(executable_code.encode()).decode()
                # First compile - capture errors for better diagnostics
                command = ['sh', '-c', f'''
echo "{encoded_code}" | base64 -d > /tmp/solution.cpp && \
if g++ -std=c++17 -O2 /tmp/solution.cpp -o /tmp/solution 2>&1; then
    /tmp/solution
else
    echo "COMPILATION_FAILED"
    exit 2
fi
''']
            elif self.language == 'csharp':
                # For C#, create minimal project and compile
                import base64
                encoded_code = base64.b64encode(executable_code.encode()).decode()
                # Create minimal .csproj manually to avoid dotnet new overwriting Program.cs
                csproj_content = '''<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>
</Project>'''
                encoded_csproj = base64.b64encode(csproj_content.encode()).decode()
                command = ['sh', '-c', f'''
mkdir -p /tmp/csapp && cd /tmp/csapp && \
echo "{encoded_csproj}" | base64 -d > csapp.csproj && \
echo "{encoded_code}" | base64 -d > Program.cs && \
if dotnet build --verbosity quiet > /dev/null 2>&1; then
    dotnet run --no-build
else
    echo "COMPILATION_FAILED"
    exit 2
fi
''']
            else:
                raise ValueError(f'Unsupported language: {self.language}')

            # Run container - no network needed for any language
            network_mode = 'none'

            # Compiled languages (C#, C++) need more memory for compilation
            if self.language in ['csharp', 'cpp']:
                memory_limit = max(512, self.problem.memory_limit)
            else:
                memory_limit = self.problem.memory_limit

            container = self.docker_client.containers.run(
                docker_image,
                name=container_name,
                detach=True,
                mem_limit=f'{memory_limit}m',
                network_mode=network_mode,
                remove=False,  # Don't auto-remove so we can get logs
                environment=environment,
                stdin_open=True,
                tty=False,
                command=command
            )

            # Wait for container to finish (with timeout)
            # Add extra time for compiled languages (C#, C++) to account for compilation
            base_timeout = self.problem.time_limit / 1000.0  # Convert ms to seconds
            compilation_overhead = 10 if self.language in ['csharp', 'cpp'] else 0  # Extra 10s for compiled languages
            timeout = base_timeout + compilation_overhead + 2  # Base + overhead + buffer
            try:
                result = container.wait(timeout=timeout)
                execution_time = int((time.time() - start_time) * 1000)  # Convert to ms

                # Get output
                output = container.logs().decode('utf-8').strip()

                # Clean up container
                try:
                    container.remove(force=True)
                except Exception:
                    pass  # Ignore cleanup errors

                # Check if execution time exceeded
                # For compiled languages (C#, C++), add compilation overhead to time limit
                time_limit = self.problem.time_limit
                if self.language in ['csharp', 'cpp']:
                    time_limit += 7000  # Add 7 seconds for compilation overhead

                if execution_time > time_limit:
                    return {
                        'passed': False,
                        'status': 'time_limit_exceeded',
                        'execution_time': execution_time,
                        'input': test_input,
                        'expected': expected_output,
                        'actual': output[:1000],  # Limit output size
                        'is_hidden': test_case.is_hidden
                    }

                # Check exit code
                if result['StatusCode'] != 0:
                    # Check if this is a compilation error (exit code 2 or COMPILATION_FAILED in output)
                    is_compilation_error = result['StatusCode'] == 2 or 'COMPILATION_FAILED' in output

                    return {
                        'passed': False,
                        'status': 'compilation_error' if is_compilation_error else 'runtime_error',
                        'execution_time': execution_time,
                        'input': test_input,
                        'expected': expected_output,
                        'actual': output[:1000],
                        'error': 'Compilation failed' if is_compilation_error else 'Program exited with non-zero status',
                        'is_hidden': test_case.is_hidden
                    }

                # Compare output - try JSON comparison first, fall back to string comparison
                actual_output = output.strip()
                passed = False

                # Try to parse both as JSON and compare objects
                try:
                    actual_obj = json.loads(actual_output)
                    expected_obj = json.loads(expected_output)
                    passed = actual_obj == expected_obj
                except (json.JSONDecodeError, ValueError):
                    # If not valid JSON, fall back to string comparison
                    passed = actual_output == expected_output

                return {
                    'passed': passed,
                    'status': 'passed' if passed else 'wrong_answer',
                    'execution_time': execution_time,
                    'input': test_input if not test_case.is_hidden else 'Hidden',
                    'expected': expected_output if not test_case.is_hidden else 'Hidden',
                    'actual': actual_output[:1000] if not test_case.is_hidden else 'Hidden',
                    'is_hidden': test_case.is_hidden
                }

            except docker.errors.ContainerError as e:
                # Clean up container
                try:
                    container.remove(force=True)
                except Exception:
                    pass

                # Check if this is a compilation error
                error_str = str(e)
                is_compilation_error = 'COMPILATION_FAILED' in error_str or e.exit_status == 2

                return {
                    'passed': False,
                    'status': 'compilation_error' if is_compilation_error else 'runtime_error',
                    'input': test_input if not test_case.is_hidden else 'Hidden',
                    'error': str(e)[:500],
                    'is_hidden': test_case.is_hidden
                }
            except Exception as e:
                # Check if this is a timeout error
                error_str = str(e).lower()
                is_timeout = 'timeout' in error_str or 'timed out' in error_str

                # Clean up container on any error
                try:
                    container.remove(force=True)
                except Exception:
                    pass

                return {
                    'passed': False,
                    'status': 'time_limit_exceeded' if is_timeout else 'internal_error',
                    'input': test_input if not test_case.is_hidden else 'Hidden',
                    'error': 'Time limit exceeded' if is_timeout else str(e)[:500],
                    'is_hidden': test_case.is_hidden
                }

        except docker.errors.ImageNotFound:
            return {
                'passed': False,
                'status': 'internal_error',
                'error': f'Docker image not found: {docker_image}',
                'is_hidden': test_case.is_hidden
            }
        except Exception as e:
            return {
                'passed': False,
                'status': 'internal_error',
                'error': str(e)[:500],
                'is_hidden': test_case.is_hidden
            }

    def _prepare_executable_code(self, test_input):
        """
        Prepare executable code by wrapping user code with test harness.

        Args:
            test_input: Test input data as string

        Returns:
            str: Complete executable code
        """
        if self.language == 'python':
            return self._prepare_python_code(test_input)
        elif self.language == 'javascript':
            return self._prepare_javascript_code(test_input)
        elif self.language == 'csharp':
            return self._prepare_csharp_code(test_input)
        elif self.language == 'cpp':
            return self._prepare_cpp_code(test_input)
        else:
            return self.code

    def _prepare_python_code(self, test_input):
        """Prepare Python code with test harness."""
        import re
        func_match = re.search(r'def\s+(\w+)\s*\(([^)]*)\)', self.code)
        if not func_match:
            return self.code

        func_name = func_match.group(1)
        params_str = func_match.group(2).strip()

        # Count parameters
        if not params_str:
            param_count = 0
        else:
            param_count = params_str.count(',') + 1

        wrapper = f'''
{self.code}

# Test harness
import json
import sys

test_input = {repr(test_input)}

try:
    # Smart input parsing based on parameter count
    if '{param_count}' == '0':
        args = []
    elif '{param_count}' == '1':
        # Single parameter - check if it's an array or single value
        if test_input.strip().startswith('['):
            import ast
            args = [ast.literal_eval(test_input.strip())]
        else:
            # Try to parse as number, fallback to string
            arg = test_input.strip()
            try:
                if '.' in arg:
                    args = [float(arg)]
                else:
                    args = [int(arg)]
            except ValueError:
                # It's a string - use as-is
                args = [arg]
    else:
        # Multiple parameters - split by comma carefully
        import ast
        try:
            # Try to parse as Python literal list first
            args = ast.literal_eval(f"[{{test_input}}]")
        except:
            # Fallback: split by comma (for simple cases like "1,2,3")
            args = []
            parts = test_input.split(',')
            for part in parts:
                part = part.strip()
                try:
                    if '.' in part:
                        args.append(float(part))
                    else:
                        args.append(int(part))
                except ValueError:
                    args.append(part)

    # Call the function
    result = {func_name}(*args)

    # Print result in expected format (without spaces for lists)
    if isinstance(result, (list, dict)):
        print(json.dumps(result, separators=(',', ':')))
    else:
        print(result)

except Exception as e:
    print(f"Error: {{e}}", file=sys.stderr)
    sys.exit(1)
'''
        return wrapper

    def _prepare_javascript_code(self, test_input):
        """Prepare JavaScript code with test harness."""
        import re
        func_match = re.search(r'function\s+(\w+)\s*\(([^)]*)\)', self.code)
        if not func_match:
            return self.code

        func_name = func_match.group(1)
        params_str = func_match.group(2).strip()

        # Count parameters
        if not params_str:
            param_count = 0
        else:
            param_count = params_str.count(',') + 1

        # Escape test_input for JavaScript (use JSON.stringify for safety)
        import json
        escaped_input = json.dumps(test_input)

        # Use .format() to avoid f-string brace escaping issues
        wrapper_template = '''
{user_code}

// Test harness
const testInput = ESCAPED_INPUT;

try {
    let args;

    // Smart input parsing based on parameter count
    if ({param_count} === 0) {
        args = [];
    } else if ({param_count} === 1) {
        // Single parameter - check if it's an array or single value
        if (testInput.trim().startsWith('[')) {
            args = [JSON.parse(testInput.trim())];
        } else {
            // Try to parse as number, fallback to string
            const arg = testInput.trim();
            const num = Number(arg);
            args = [!isNaN(num) && arg !== '' ? num : arg];
        }
    } else {
        // Multiple parameters - try JSON parse first
        try {
            args = JSON.parse('[' + testInput + ']');
        } catch {
            // Fallback: split by comma for simple cases
            args = testInput.split(',').map(arg => {
                arg = arg.trim();
                const num = Number(arg);
                if (!isNaN(num) && arg !== '') return num;
                return arg.replace(/^["']|["']$/g, '');
            });
        }
    }

    // Call the function
    const result = FUNC_NAME(...args);

    // Print result with proper formatting
    if (Array.isArray(result) || (typeof result === 'object' && result !== null)) {
        console.log(JSON.stringify(result));
    } else if (typeof result === 'boolean') {
        // Capitalize boolean to match Python True/False
        console.log(result ? 'True' : 'False');
    } else {
        console.log(result);
    }

} catch (e) {
    console.error('Error:', e.message);
    process.exit(1);
}
'''
        wrapper = wrapper_template.replace('{user_code}', self.code)\
                                  .replace('ESCAPED_INPUT', escaped_input)\
                                  .replace('FUNC_NAME', func_name)\
                                  .replace('{param_count}', str(param_count))
        return wrapper

    def _prepare_csharp_code(self, test_input):
        """Prepare C# code with test harness."""
        import re
        import sys

        # Find the function signature - handle return types like int[], List<int>, etc.
        # Match: public static RETURN_TYPE FUNC_NAME(PARAMS)
        func_match = re.search(r'public\s+static\s+([\w\[\]<>,\s]+?)\s+(\w+)\s*\(([^)]*)\)', self.code)
        if not func_match:
            # If regex fails, return code as-is (will cause compilation error with helpful message)
            return self.code

        func_name = func_match.group(2)
        params_str = func_match.group(3).strip()

        # Count the number of parameters
        if not params_str:
            param_count = 0
        else:
            # Count commas and add 1 (e.g., "int a, int b" has 1 comma = 2 params)
            param_count = params_str.count(',') + 1

        # Extract using statements from user code
        user_lines = self.code.split('\n')
        using_statements = []
        code_lines = []
        has_class_definition = False

        for line in user_lines:
            stripped = line.strip()
            if stripped.startswith('using ') and ';' in stripped:
                using_statements.append(line)
            else:
                code_lines.append(line)
                # Check if user code already has a class definition
                if 'class ' in stripped and '{' in stripped:
                    has_class_definition = True

        # Build C# code using simple string concatenation to avoid escaping issues
        wrapper = 'using System;\n'
        wrapper += 'using System.Linq;\n'
        wrapper += 'using System.Text.Json;\n'
        wrapper += 'using System.Collections.Generic;\n'

        # Add user's using statements (avoid duplicates)
        for using_stmt in using_statements:
            if using_stmt.strip() not in ['using System;', 'using System.Linq;',
                                          'using System.Text.Json;', 'using System.Collections.Generic;']:
                wrapper += using_stmt + '\n'

        wrapper += '\n'

        # If user code already has a class, use it directly; otherwise wrap it
        if has_class_definition:
            wrapper += '// User solution class\n'
            wrapper += '\n'.join(code_lines) + '\n\n'
        else:
            # Indent user code properly (without using statements)
            indented_code = '\n'.join('    ' + line if line.strip() else line
                                      for line in code_lines)
            wrapper += '// User solution class\n'
            wrapper += 'class Solution {\n'
            wrapper += indented_code + '\n'
            wrapper += '}\n\n'
        wrapper += '// Test harness\n'
        wrapper += 'class Program {\n'
        wrapper += '    static void Main() {\n'
        # Escape double quotes for C# verbatim string (@ prefix)
        escaped_input = test_input.replace('"', '""')
        wrapper += f'        string testInput = @"{escaped_input}";\n\n'
        wrapper += '        try {\n'
        wrapper += '            object result;\n\n'

        # Generate code based on parameter count
        if param_count == 1:
            wrapper += '            // Single argument (could be array, int, or string)\n'
            wrapper += '            dynamic arg;\n'
            wrapper += '            if (testInput.Trim().StartsWith("[")) {\n'
            wrapper += '                arg = System.Text.Json.JsonSerializer.Deserialize<int[]>(testInput.Trim());\n'
            wrapper += '            } else if (int.TryParse(testInput.Trim(), out int intVal)) {\n'
            wrapper += '                arg = intVal;\n'
            wrapper += '            } else {\n'
            wrapper += '                arg = testInput.Trim();  // string\n'
            wrapper += '            }\n'
            wrapper += f'            result = Solution.{func_name}(arg);\n\n'
        elif param_count == 2:
            wrapper += '            // Two arguments - smart split that respects brackets\n'
            wrapper += '            var parts = new List<string>();\n'
            wrapper += '            int depth = 0, start = 0;\n'
            wrapper += '            for (int i = 0; i < testInput.Length; i++) {\n'
            wrapper += '                if (testInput[i] == \'[\') depth++;\n'
            wrapper += '                else if (testInput[i] == \']\') depth--;\n'
            wrapper += '                else if (testInput[i] == \',\' && depth == 0) {\n'
            wrapper += '                    parts.Add(testInput.Substring(start, i - start).Trim());\n'
            wrapper += '                    start = i + 1;\n'
            wrapper += '                }\n'
            wrapper += '            }\n'
            wrapper += '            if (start < testInput.Length) parts.Add(testInput.Substring(start).Trim());\n\n'
            wrapper += '            if (parts.Count != 2) {\n'
            wrapper += '                throw new Exception("Expected 2 arguments, got: " + parts.Count);\n'
            wrapper += '            }\n\n'
            wrapper += '            // Parse first argument (could be array, int, or string)\n'
            wrapper += '            dynamic arg1;\n'
            wrapper += '            if (parts[0].StartsWith("[")) {\n'
            wrapper += '                arg1 = System.Text.Json.JsonSerializer.Deserialize<int[]>(parts[0]);\n'
            wrapper += '            } else if (int.TryParse(parts[0], out int intVal1)) {\n'
            wrapper += '                arg1 = intVal1;\n'
            wrapper += '            } else {\n'
            wrapper += '                arg1 = parts[0];  // string\n'
            wrapper += '            }\n\n'
            wrapper += '            // Parse second argument (could be array, int, or string)\n'
            wrapper += '            dynamic arg2;\n'
            wrapper += '            if (parts[1].StartsWith("[")) {\n'
            wrapper += '                arg2 = System.Text.Json.JsonSerializer.Deserialize<int[]>(parts[1]);\n'
            wrapper += '            } else if (int.TryParse(parts[1], out int intVal2)) {\n'
            wrapper += '                arg2 = intVal2;\n'
            wrapper += '            } else {\n'
            wrapper += '                arg2 = parts[1];  // string\n'
            wrapper += '            }\n\n'
            wrapper += f'            result = Solution.{func_name}(arg1, arg2);\n\n'
        elif param_count == 3:
            wrapper += '            // Three arguments - smart split that respects brackets\n'
            wrapper += '            var parts = new List<string>();\n'
            wrapper += '            int depth = 0, start = 0;\n'
            wrapper += '            for (int i = 0; i < testInput.Length; i++) {\n'
            wrapper += '                if (testInput[i] == \'[\') depth++;\n'
            wrapper += '                else if (testInput[i] == \']\') depth--;\n'
            wrapper += '                else if (testInput[i] == \',\' && depth == 0) {\n'
            wrapper += '                    parts.Add(testInput.Substring(start, i - start).Trim());\n'
            wrapper += '                    start = i + 1;\n'
            wrapper += '                }\n'
            wrapper += '            }\n'
            wrapper += '            if (start < testInput.Length) parts.Add(testInput.Substring(start).Trim());\n\n'
            wrapper += '            if (parts.Count != 3) {\n'
            wrapper += '                throw new Exception("Expected 3 arguments, got: " + parts.Count);\n'
            wrapper += '            }\n\n'
            wrapper += '            // Parse arguments (could be array, int, or string)\n'
            wrapper += '            dynamic arg1;\n'
            wrapper += '            if (parts[0].StartsWith("[")) {\n'
            wrapper += '                arg1 = System.Text.Json.JsonSerializer.Deserialize<int[]>(parts[0]);\n'
            wrapper += '            } else if (int.TryParse(parts[0], out int intVal1)) {\n'
            wrapper += '                arg1 = intVal1;\n'
            wrapper += '            } else {\n'
            wrapper += '                arg1 = parts[0];  // string\n'
            wrapper += '            }\n\n'
            wrapper += '            dynamic arg2;\n'
            wrapper += '            if (parts[1].StartsWith("[")) {\n'
            wrapper += '                arg2 = System.Text.Json.JsonSerializer.Deserialize<int[]>(parts[1]);\n'
            wrapper += '            } else if (int.TryParse(parts[1], out int intVal2)) {\n'
            wrapper += '                arg2 = intVal2;\n'
            wrapper += '            } else {\n'
            wrapper += '                arg2 = parts[1];  // string\n'
            wrapper += '            }\n\n'
            wrapper += '            dynamic arg3;\n'
            wrapper += '            if (parts[2].StartsWith("[")) {\n'
            wrapper += '                arg3 = System.Text.Json.JsonSerializer.Deserialize<int[]>(parts[2]);\n'
            wrapper += '            } else if (int.TryParse(parts[2], out int intVal3)) {\n'
            wrapper += '                arg3 = intVal3;\n'
            wrapper += '            } else {\n'
            wrapper += '                arg3 = parts[2];  // string\n'
            wrapper += '            }\n\n'
            wrapper += f'            result = Solution.{func_name}(arg1, arg2, arg3);\n\n'
        else:
            wrapper += f'            throw new Exception("Unsupported parameter count: {param_count}");\n\n'
        wrapper += '            // Print result in correct format (JSON for arrays/objects)\n'
        wrapper += '            if (result is System.Collections.IEnumerable && !(result is string)) {\n'
        wrapper += '                Console.WriteLine(System.Text.Json.JsonSerializer.Serialize(result));\n'
        wrapper += '            } else {\n'
        wrapper += '                Console.WriteLine(result);\n'
        wrapper += '            }\n'
        wrapper += '        } catch (Exception e) {\n'
        wrapper += '            Console.Error.WriteLine("Error: " + e.Message);\n'
        wrapper += '            Console.Error.WriteLine("Stack: " + e.StackTrace);\n'
        wrapper += '            Environment.Exit(1);\n'
        wrapper += '        }\n'
        wrapper += '    }\n'
        wrapper += '}\n'

        return wrapper

    def _prepare_cpp_code(self, test_input):
        """Prepare C++ code with test harness."""
        import re

        # Check if user code already has main() - if so, return as-is
        if re.search(r'\bint\s+main\s*\(', self.code):
            return self.code

        # Find the function signature - look for pattern: TYPE name(params) {
        # We'll extract the full line and parse it
        lines = self.code.split('\n')
        func_line = None
        func_name = None
        return_type = None
        params_str = None

        for i, line in enumerate(lines):
            # Look for function definition (has opening paren and likely opening brace or semicolon)
            if '(' in line and not line.strip().startswith('//') and not line.strip().startswith('#'):
                # Try to extract function signature
                # Match: TYPE functionName(params...)
                # We need to handle nested templates in params, so we'll match differently
                stripped = line.strip()

                # Find the function name and opening paren
                paren_idx = stripped.find('(')
                if paren_idx == -1:
                    continue

                # Everything before '(' should be "RETURN_TYPE FUNC_NAME"
                before_paren = stripped[:paren_idx].strip()
                parts = before_paren.split()
                if len(parts) < 2:
                    continue

                potential_name = parts[-1]  # Last word is function name
                potential_return = ' '.join(parts[:-1])  # Everything else is return type

                # Find matching closing paren (handling nested parens)
                depth = 0
                close_paren_idx = -1
                for j in range(paren_idx, len(stripped)):
                    if stripped[j] == '(':
                        depth += 1
                    elif stripped[j] == ')':
                        depth -= 1
                        if depth == 0:
                            close_paren_idx = j
                            break

                if close_paren_idx == -1:
                    continue

                potential_params = stripped[paren_idx+1:close_paren_idx]

                # Skip invalid keywords
                invalid_keywords = ['if', 'while', 'for', 'switch', 'using', 'namespace', 'class', 'struct', 'template', 'return']
                if not any(potential_return.startswith(kw) for kw in invalid_keywords):
                    return_type = potential_return
                    func_name = potential_name
                    params_str = potential_params.strip()
                    break

        if not func_name:
            return self.code

        # Parse parameter types
        param_types = []
        if params_str:
            # Split by comma and extract types
            params = [p.strip() for p in params_str.split(',')]
            for param in params:
                # Extract type (first word(s) before variable name)
                parts = param.split()
                if len(parts) >= 2:
                    param_type = ' '.join(parts[:-1])  # Everything except last word
                    param_types.append(param_type)
                else:
                    param_types.append('int')  # default

        # Build C++ code
        wrapper = '#include <iostream>\n'
        wrapper += '#include <string>\n'
        wrapper += '#include <sstream>\n'
        wrapper += '#include <algorithm>\n'
        wrapper += '#include <vector>\n'
        wrapper += '#include <unordered_map>\n'
        wrapper += 'using namespace std;\n\n'
        wrapper += '// Helper function to parse vector<int> from string like "[1,2,3]"\n'
        wrapper += 'vector<int> parseVector(const string& s) {\n'
        wrapper += '    vector<int> result;\n'
        wrapper += '    if (s.empty() || s == "[]") return result;\n'
        wrapper += '    stringstream ss(s.substr(1, s.length() - 2));\n'
        wrapper += '    string item;\n'
        wrapper += '    while (getline(ss, item, \',\')) {\n'
        wrapper += '        result.push_back(stoi(item));\n'
        wrapper += '    }\n'
        wrapper += '    return result;\n'
        wrapper += '}\n\n'
        wrapper += '// Helper function to parse vector<vector<int>> from string like "[[1,2],[3]]"\n'
        wrapper += 'vector<vector<int>> parseVector2D(const string& s) {\n'
        wrapper += '    vector<vector<int>> result;\n'
        wrapper += '    if (s.empty() || s == "[]") return result;\n'
        wrapper += '    int depth = 0, start = -1;\n'
        wrapper += '    for (int i = 0; i < s.length(); i++) {\n'
        wrapper += '        if (s[i] == \'[\') {\n'
        wrapper += '            depth++;\n'
        wrapper += '            if (depth == 2) start = i;\n'
        wrapper += '        } else if (s[i] == \']\') {\n'
        wrapper += '            if (depth == 2) {\n'
        wrapper += '                result.push_back(parseVector(s.substr(start, i - start + 1)));\n'
        wrapper += '            }\n'
        wrapper += '            depth--;\n'
        wrapper += '        }\n'
        wrapper += '    }\n'
        wrapper += '    return result;\n'
        wrapper += '}\n\n'
        wrapper += '// Helper function to split input by comma (top level only)\n'
        wrapper += 'vector<string> splitInput(const string& s) {\n'
        wrapper += '    vector<string> result;\n'
        wrapper += '    int depth = 0, start = 0;\n'
        wrapper += '    for (int i = 0; i < s.length(); i++) {\n'
        wrapper += '        if (s[i] == \'[\') depth++;\n'
        wrapper += '        else if (s[i] == \']\') depth--;\n'
        wrapper += '        else if (s[i] == \',\' && depth == 0) {\n'
        wrapper += '            result.push_back(s.substr(start, i - start));\n'
        wrapper += '            start = i + 1;\n'
        wrapper += '            while (start < s.length() && s[start] == \' \') start++;\n'
        wrapper += '        }\n'
        wrapper += '    }\n'
        wrapper += '    if (start < s.length()) result.push_back(s.substr(start));\n'
        wrapper += '    return result;\n'
        wrapper += '}\n\n'
        wrapper += '// Helper function to print vectors in JSON format\n'
        wrapper += 'template<typename T>\n'
        wrapper += 'void printVector(const vector<T>& vec) {\n'
        wrapper += '    cout << "[";\n'
        wrapper += '    for (size_t i = 0; i < vec.size(); i++) {\n'
        wrapper += '        if (i > 0) cout << ",";\n'
        wrapper += '        cout << vec[i];\n'
        wrapper += '    }\n'
        wrapper += '    cout << "]";\n'
        wrapper += '}\n\n'
        wrapper += '// Helper function to print 2D vectors\n'
        wrapper += 'template<typename T>\n'
        wrapper += 'void printVector2D(const vector<vector<T>>& vec) {\n'
        wrapper += '    cout << "[";\n'
        wrapper += '    for (size_t i = 0; i < vec.size(); i++) {\n'
        wrapper += '        if (i > 0) cout << ",";\n'
        wrapper += '        printVector(vec[i]);\n'
        wrapper += '    }\n'
        wrapper += '    cout << "]";\n'
        wrapper += '}\n\n'
        wrapper += '// User solution\n'
        wrapper += self.code + '\n\n'
        wrapper += '// Test harness\n'
        wrapper += 'int main() {\n'
        wrapper += f'    string testInput = "{test_input}";\n\n'
        wrapper += '    try {\n'

        # Generate code based on parameter count and types
        param_count = len(param_types)

        if param_count == 0:
            wrapper += f'        auto result = {func_name}();\n'
            # Check return type and print accordingly
            if 'vector<vector' in return_type:
                wrapper += '        printVector2D(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'vector' in return_type:
                wrapper += '        printVector(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'bool' in return_type:
                wrapper += '        cout << (result ? "True" : "False") << endl;\n\n'
            else:
                wrapper += '        cout << result << endl;\n\n'
        elif param_count == 1:
            param_type = param_types[0]
            wrapper += '        // Single argument\n'

            if 'vector<vector' in param_type:
                wrapper += '        auto arg = parseVector2D(testInput);\n'
            elif 'vector' in param_type:
                wrapper += '        auto arg = parseVector(testInput);\n'
            elif 'unordered_map' in param_type or 'map' in param_type:
                # For map types, treat as 2D vector
                wrapper += '        auto arg_vec = parseVector2D(testInput);\n'
                wrapper += '        unordered_map<int, vector<int>> arg;\n'
                wrapper += '        for (int i = 0; i < arg_vec.size(); i++) {\n'
                wrapper += '            arg[i] = arg_vec[i];\n'
                wrapper += '        }\n'
            elif 'string' in param_type:
                wrapper += '        string arg = testInput;\n'
            elif 'int' in param_type:
                wrapper += '        int arg = stoi(testInput);\n'
            elif 'long' in param_type:
                wrapper += '        long arg = stol(testInput);\n'
            elif 'double' in param_type or 'float' in param_type:
                wrapper += '        double arg = stod(testInput);\n'
            else:
                wrapper += '        auto arg = testInput;  // fallback\n'

            wrapper += f'        auto result = {func_name}(arg);\n'
            # Check return type and print accordingly
            if 'vector<vector' in return_type:
                wrapper += '        printVector2D(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'vector' in return_type:
                wrapper += '        printVector(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'bool' in return_type:
                wrapper += '        cout << (result ? "True" : "False") << endl;\n\n'
            else:
                wrapper += '        cout << result << endl;\n\n'

        elif param_count == 2:
            wrapper += '        // Two arguments\n'
            wrapper += '        vector<string> parts = splitInput(testInput);\n'
            wrapper += '        if (parts.size() != 2) {\n'
            wrapper += '            cerr << "Expected 2 arguments, got: " << parts.size() << endl;\n'
            wrapper += '            return 1;\n'
            wrapper += '        }\n\n'

            # Parse first argument
            param_type1 = param_types[0]
            if 'vector<vector' in param_type1:
                wrapper += '        auto arg1 = parseVector2D(parts[0]);\n'
            elif 'vector' in param_type1:
                wrapper += '        auto arg1 = parseVector(parts[0]);\n'
            elif 'unordered_map' in param_type1 or 'map' in param_type1:
                # For map types, treat as 2D vector for now
                wrapper += '        auto arg1_vec = parseVector2D(parts[0]);\n'
                wrapper += '        unordered_map<int, vector<int>> arg1;\n'
                wrapper += '        for (int i = 0; i < arg1_vec.size(); i++) {\n'
                wrapper += '            arg1[i] = arg1_vec[i];\n'
                wrapper += '        }\n'
            elif 'string' in param_type1:
                wrapper += '        string arg1 = parts[0];\n'
            elif 'int' in param_type1:
                wrapper += '        int arg1 = stoi(parts[0]);\n'
            elif 'long' in param_type1:
                wrapper += '        long arg1 = stol(parts[0]);\n'
            else:
                wrapper += '        auto arg1 = parts[0];\n'

            # Parse second argument
            param_type2 = param_types[1]
            if 'vector<vector' in param_type2:
                wrapper += '        auto arg2 = parseVector2D(parts[1]);\n'
            elif 'vector' in param_type2:
                wrapper += '        auto arg2 = parseVector(parts[1]);\n'
            elif 'string' in param_type2:
                wrapper += '        string arg2 = parts[1];\n'
            elif 'int' in param_type2:
                wrapper += '        int arg2 = stoi(parts[1]);\n'
            elif 'long' in param_type2:
                wrapper += '        long arg2 = stol(parts[1]);\n'
            else:
                wrapper += '        auto arg2 = parts[1];\n'

            wrapper += f'        auto result = {func_name}(arg1, arg2);\n'
            # Check return type and print accordingly
            if 'vector<vector' in return_type:
                wrapper += '        printVector2D(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'vector' in return_type:
                wrapper += '        printVector(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'bool' in return_type:
                wrapper += '        cout << (result ? "True" : "False") << endl;\n\n'
            else:
                wrapper += '        cout << result << endl;\n\n'
        elif param_count == 3:
            wrapper += '        // Three arguments\n'
            wrapper += '        vector<string> parts = splitInput(testInput);\n'
            wrapper += '        if (parts.size() != 3) {\n'
            wrapper += '            cerr << "Expected 3 arguments, got: " << parts.size() << endl;\n'
            wrapper += '            return 1;\n'
            wrapper += '        }\n\n'

            # Parse all 3 arguments generically (string or int)
            for i in range(3):
                wrapper += f'        // Parse argument {i+1}\n'
                if i < len(param_types):
                    param_type = param_types[i]
                    if 'string' in param_type:
                        wrapper += f'        string arg{i+1} = parts[{i}];\n'
                    elif 'int' in param_type:
                        wrapper += f'        int arg{i+1} = stoi(parts[{i}]);\n'
                    else:
                        wrapper += f'        auto arg{i+1} = parts[{i}];\n'
                else:
                    wrapper += f'        auto arg{i+1} = parts[{i}];\n'

            wrapper += f'\n        auto result = {func_name}(arg1, arg2, arg3);\n'
            # Check return type and print accordingly
            if 'vector<vector' in return_type:
                wrapper += '        printVector2D(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'vector' in return_type:
                wrapper += '        printVector(result);\n'
                wrapper += '        cout << endl;\n\n'
            elif 'bool' in return_type:
                wrapper += '        cout << (result ? "True" : "False") << endl;\n\n'
            else:
                wrapper += '        cout << result << endl;\n\n'
        else:
            # For 4+ parameters, generate generic code
            wrapper += f'        cerr << "Unsupported parameter count: {param_count}" << endl;\n'
            wrapper += '        return 1;\n'

        wrapper += '    } catch (const exception& e) {\n'
        wrapper += '        cerr << "Error: " << e.what() << endl;\n'
        wrapper += '        return 1;\n'
        wrapper += '    }\n'
        wrapper += '    return 0;\n'
        wrapper += '}\n'

        return wrapper

    def _determine_status(self, test_results):
        """
        Determine submission status from test results.

        Args:
            test_results: List of test case results

        Returns:
            str: Status code
        """
        for result in test_results:
            status = result.get('status')
            if status in ['time_limit_exceeded', 'memory_limit_exceeded', 'runtime_error', 'compilation_error']:
                return status
        return 'wrong_answer'

    def _get_error_message(self, test_results):
        """
        Get error message from failed test.

        Args:
            test_results: List of test case results

        Returns:
            str: Error message
        """
        for result in test_results:
            if not result.get('passed', False):
                error = result.get('error', '')
                if error:
                    return error
                return f"Test case failed. Expected: {result.get('expected', 'N/A')}, Got: {result.get('actual', 'N/A')}"
        return ''
