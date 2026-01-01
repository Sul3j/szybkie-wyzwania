"""
Pytest configuration and shared fixtures for all tests.
"""
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.accounts.models import UserProfile
from apps.problems.models import Problem, TestCase, ProblemTag
from apps.submissions.models import Submission

User = get_user_model()


@pytest.fixture
def api_client():
    """Return API client for making requests."""
    return APIClient()


@pytest.fixture
def user(db):
    """Create a test user with profile."""
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    return user


@pytest.fixture
def user2(db):
    """Create a second test user."""
    user = User.objects.create_user(
        username='testuser2',
        email='test2@example.com',
        password='testpass123'
    )
    return user


@pytest.fixture
def admin_user(db):
    """Create an admin user."""
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123'
    )
    return user


@pytest.fixture
def authenticated_client(api_client, user):
    """Return authenticated API client."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def admin_client(api_client, admin_user):
    """Return authenticated admin API client."""
    api_client.force_authenticate(user=admin_user)
    return api_client


@pytest.fixture
def problem(db, admin_user):
    """Create a test problem."""
    problem = Problem.objects.create(
        title='Two Sum',
        slug='two-sum',
        description='Add two numbers.',
        difficulty='easy',
        points=10,
        created_by=admin_user,
        function_signature_python='def add(a: int, b: int) -> int:',
        function_signature_javascript='function add(a, b) {',
        function_signature_csharp='public static int Add(int a, int b) {',
        function_signature_cpp='int add(int a, int b) {',
    )
    return problem


@pytest.fixture
def problem_with_tests(problem):
    """Create a problem with test cases."""
    TestCase.objects.create(
        problem=problem,
        input_data='5, 3',
        expected_output='8',
        is_hidden=False
    )
    TestCase.objects.create(
        problem=problem,
        input_data='10, 20',
        expected_output='30',
        is_hidden=True
    )
    return problem


@pytest.fixture
def submission(db, user, problem_with_tests):
    """Create a test submission."""
    submission = Submission.objects.create(
        user=user,
        problem=problem_with_tests,
        code='def add(a, b):\\n    return a + b',
        language='python',
        status='pending'
    )
    return submission


@pytest.fixture
def mock_docker(mocker):
    """Mock Docker client for testing evaluator."""
    mock_client = mocker.MagicMock()
    mock_container = mocker.MagicMock()
    mock_container.wait.return_value = {'StatusCode': 0}
    mock_container.logs.return_value = b'8\\n'
    mock_client.containers.run.return_value = mock_container
    mocker.patch('docker.from_env', return_value=mock_client)
    return mock_client


@pytest.fixture
def mock_celery(mocker):
    """Mock Celery tasks for testing without async execution."""
    mock_task = mocker.patch('apps.judge.tasks.evaluate_submission.delay')
    return mock_task


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Enable database access for all tests automatically."""
    pass
