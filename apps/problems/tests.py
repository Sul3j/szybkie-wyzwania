"""
Tests for problems app - Problems, Test Cases, Tags
"""
import pytest
from django.urls import reverse
from rest_framework import status
from apps.problems.models import Problem, TestCase, ProblemTag


@pytest.mark.unit
class TestProblemModel:
    """Test Problem model."""

    def test_problem_creation(self, problem):
        """Test problem is created correctly."""
        assert problem.title == 'Two Sum'
        assert problem.slug == 'two-sum'
        assert problem.difficulty == 'easy'
        assert problem.points == 10

    def test_problem_string_representation(self, problem):
        """Test __str__ method."""
        assert str(problem) == 'Two Sum (easy)'

    def test_test_case_creation(self, problem_with_tests):
        """Test creating test cases for problem."""
        test_cases = problem_with_tests.test_cases.all()
        assert test_cases.count() == 2
        assert test_cases.filter(is_hidden=False).count() == 1
        assert test_cases.filter(is_hidden=True).count() == 1


@pytest.mark.integration
class TestProblemAPI:
    """Test Problem API endpoints."""

    def test_list_problems(self, api_client, problem):
        """Test listing problems."""
        url = reverse('problem-list')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1

    def test_get_problem_detail(self, api_client, problem_with_tests):
        """Test getting problem detail."""
        url = reverse('problem-detail', kwargs={'slug': problem_with_tests.slug})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Two Sum'
        # Should only show non-hidden test cases
        visible_tests = [t for t in response.data['test_cases'] if not t['is_hidden']]
        assert len(visible_tests) == 1

    def test_create_problem_as_admin(self, admin_client):
        """Test creating problem as admin."""
        url = reverse('problem-create')
        data = {
            'title': 'New Problem',
            'description': 'Test problem',
            'difficulty': 'medium',
            'points': 20,
            'function_signature_python': 'def solve():',
        }

        response = admin_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Problem.objects.filter(title='New Problem').exists()

    def test_create_problem_as_user_forbidden(self, authenticated_client):
        """Test creating problem as regular user fails."""
        url = reverse('problem-create')
        data = {'title': 'New Problem'}

        response = authenticated_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_filter_problems_by_difficulty(self, api_client, problem):
        """Test filtering problems by difficulty."""
        url = reverse('problem-list') + '?difficulty=easy'
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        for p in response.data['results']:
            assert p['difficulty'] == 'easy'

    def test_random_problem(self, api_client, problem):
        """Test getting random problem."""
        url = reverse('problem-random')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert 'title' in response.data
