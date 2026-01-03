#!/usr/bin/env python3
import json
import os
import resource
import signal
import sys


def set_limits():
    """Set resource limits for the process."""
    # CPU time limit (in seconds)
    time_limit = int(os.environ.get("TIME_LIMIT", 2000)) // 1000
    resource.setrlimit(resource.RLIMIT_CPU, (time_limit, time_limit))

    # Memory limit (in bytes)
    memory_limit = int(os.environ.get("MEMORY_LIMIT", 128)) * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))


def timeout_handler(signum, frame):
    """Handle timeout signal."""
    raise TimeoutError("Execution time limit exceeded")


def run_code(code, test_input):
    """
    Execute user code with test input.

    Args:
        code: User's code string
        test_input: Input data for the test case

    Returns:
        str: Output from the code execution
    """
    # Restricted imports - only allow safe modules
    allowed_modules = {
        "math",
        "random",
        "itertools",
        "collections",
        "functools",
        "operator",
        "string",
        "re",
        "datetime",
        "json",
        "heapq",
        "bisect",
    }

    # Create restricted globals
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "bool": bool,
            "max": max,
            "min": min,
            "sum": sum,
            "abs": abs,
            "sorted": sorted,
            "enumerate": enumerate,
            "zip": zip,
            "map": map,
            "filter": filter,
            "all": all,
            "any": any,
        }
    }

    # Allow importing safe modules
    for module in allowed_modules:
        try:
            restricted_globals[module] = __import__(module)
        except ImportError:
            pass

    # Parse test input
    try:
        # Try to parse as JSON first
        input_data = json.loads(test_input)
    except:
        # If not JSON, use as string
        input_data = test_input

    # Prepare code execution
    restricted_globals["input_data"] = input_data

    # Execute code
    try:
        exec(code, restricted_globals)
    except Exception as e:
        print(f"Error: {type(e).__name__}: {str(e)}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point."""
    try:
        # Set resource limits
        set_limits()

        # Set timeout alarm
        time_limit = int(os.environ.get("TIME_LIMIT", 2000)) // 1000 + 1
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(time_limit)

        # Get code from stdin or environment
        code = (
            sys.stdin.read() if not sys.stdin.isatty() else os.environ.get("CODE", "")
        )

        # Get test input
        test_input = os.environ.get("TEST_INPUT", "")

        # Run the code
        run_code(code, test_input)

    except TimeoutError:
        print("Time limit exceeded", file=sys.stderr)
        sys.exit(124)  # Special exit code for timeout
    except MemoryError:
        print("Memory limit exceeded", file=sys.stderr)
        sys.exit(125)  # Special exit code for memory
    except Exception as e:
        print(f"Runtime error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
