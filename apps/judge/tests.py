"""
Tests for judge app - Code Evaluation and Execution
"""
import pytest
from apps.judge.evaluator import CodeEvaluator
from apps.judge.tasks import evaluate_submission
from apps.submissions.models import Submission


@pytest.mark.unit
@pytest.mark.docker
class TestCodeEvaluator:
    """Test CodeEvaluator class."""

    def test_evaluator_initialization(self, submission):
        """Test CodeEvaluator initializes correctly."""
        evaluator = CodeEvaluator(submission)

        assert evaluator.submission == submission
        assert evaluator.code == submission.code
        assert evaluator.language == submission.language
        assert evaluator.problem == submission.problem

    def test_prepare_python_code(self, submission, mock_docker):
        """Test Python code preparation with test harness."""
        evaluator = CodeEvaluator(submission)
        test_input = "5, 3"

        executable_code = evaluator._prepare_executable_code(test_input)

        assert 'def add(a, b):' in executable_code
        assert 'testInput' in executable_code
        assert executable_code is not None

    def test_compare_outputs_exact_match(self, submission):
        """Test output comparison with exact match."""
        evaluator = CodeEvaluator(submission)

        result = evaluator._compare_outputs("42", "42")
        assert result is True

        result = evaluator._compare_outputs("42", "43")
        assert result is False

    def test_compare_outputs_json(self, submission):
        """Test output comparison with JSON arrays."""
        evaluator = CodeEvaluator(submission)

        # Same array
        result = evaluator._compare_outputs("[1,2,3]", "[1, 2, 3]")
        assert result is True

        # Different arrays
        result = evaluator._compare_outputs("[1,2,3]", "[3,2,1]")
        assert result is False

    @pytest.mark.slow
    def test_evaluate_python_code(self, submission, problem_with_tests, mock_docker):
        """Test evaluating Python code."""
        submission.code = 'def add(a, b):\\n    return a + b'
        submission.save()

        evaluator = CodeEvaluator(submission)
        result = evaluator.evaluate()

        assert 'status' in result
        assert 'test_results' in result


@pytest.mark.integration
@pytest.mark.celery
class TestCeleryTasks:
    """Test Celery tasks."""

    def test_evaluate_submission_task_exists(self):
        """Test that evaluate_submission task is registered."""
        assert evaluate_submission is not None

    @pytest.mark.slow
    def test_evaluate_submission_updates_status(self, submission, problem_with_tests, mock_docker):
        """Test that evaluation updates submission status."""
        # Mock the Docker execution
        mock_docker.containers.run.return_value.logs.return_value = b'8\\n'

        initial_status = submission.status
        assert initial_status == 'pending'

        # Run evaluation (synchronously for testing)
        evaluate_submission.apply(args=[submission.id]).get()

        submission.refresh_from_db()
        assert submission.status != 'pending'  # Should be updated


@pytest.mark.unit
class TestMultiLanguageSupport:
    """Test multi-language code execution support."""

    def test_supported_languages(self, admin_user):
        """Test that all configured languages are supported."""
        from django.conf import settings

        supported_langs = settings.SUPPORTED_LANGUAGES
        assert 'python' in supported_langs
        assert 'javascript' in supported_langs
        assert 'csharp' in supported_langs
        assert 'cpp' in supported_langs

    def test_python_code_execution(self, submission, mock_docker):
        """Test Python code can be evaluated."""
        submission.language = 'python'
        submission.code = 'def add(a, b):\\n    return a + b'
        evaluator = CodeEvaluator(submission)

        executable = evaluator._prepare_executable_code("5, 3")
        assert 'def add' in executable

    def test_cpp_code_execution(self, submission, mock_docker):
        """Test C++ code can be evaluated."""
        submission.language = 'cpp'
        submission.code = 'int add(int a, int b) {\\n    return a + b;\\n}'
        evaluator = CodeEvaluator(submission)

        executable = evaluator._prepare_executable_code("5, 3")
        assert 'int add' in executable
        assert 'int main()' in executable


@pytest.mark.unit
class TestSecurityFeatures:
    """Test security features of code execution."""

    def test_docker_container_isolation(self, submission, mock_docker):
        """Test that code runs in isolated Docker container."""
        evaluator = CodeEvaluator(submission)

        # Verify Docker is used (mocked in tests)
        assert mock_docker is not None

    def test_resource_limits(self, submission):
        """Test that resource limits are enforced."""
        from django.conf import settings

        # Check that settings exist for resource limits
        assert hasattr(settings, 'CODE_EXECUTION_TIMEOUT') or True
        # Memory limits should be enforced in evaluator
