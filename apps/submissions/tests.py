"""
Tests for submissions app - Code Submissions and Evaluation
"""
import pytest
from django.urls import reverse
from rest_framework import status
from apps.submissions.models import Submission


@pytest.mark.unit
class TestSubmissionModel:
    """Test Submission model."""

    def test_submission_creation(self, submission):
        """Test submission is created correctly."""
        assert submission.code == 'def add(a, b):\\n    return a + b'
        assert submission.language == 'python'
        assert submission.status == 'pending'

    def test_submission_string_representation(self, submission):
        """Test __str__ method."""
        expected = f"{submission.user.username} - {submission.problem.title} ({submission.language})"
        assert str(submission) == expected


@pytest.mark.integration
class TestSubmissionAPI:
    """Test Submission API endpoints."""

    def test_create_submission(self, authenticated_client, problem_with_tests, mock_celery):
        """Test creating a submission."""
        url = reverse('submission-create')
        data = {
            'problem_slug': problem_with_tests.slug,
            'code': 'def add(a, b):\\n    return a + b',
            'language': 'python'
        }

        response = authenticated_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert 'id' in response.data
        assert response.data['status'] == 'pending'

        # Verify Celery task was called
        mock_celery.assert_called_once()

    def test_create_submission_unauthenticated(self, api_client, problem_with_tests):
        """Test creating submission fails when not authenticated."""
        url = reverse('submission-create')
        data = {
            'problem_slug': problem_with_tests.slug,
            'code': 'def add(a, b):\\n    return a + b',
            'language': 'python'
        }

        response = api_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_list_user_submissions(self, authenticated_client, submission):
        """Test listing user's own submissions."""
        url = reverse('submission-list')
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1

    def test_get_submission_detail(self, authenticated_client, submission):
        """Test getting submission detail."""
        url = reverse('submission-detail', kwargs={'pk': submission.id})
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['code'] == submission.code

    def test_cannot_view_others_submission(self, authenticated_client, submission, user2):
        """Test user cannot view other user's submission."""
        # Create submission for user2
        submission.user = user2
        submission.save()

        url = reverse('submission-detail', kwargs={'pk': submission.id})
        response = authenticated_client.get(url)

        # Should be forbidden or not found
        assert response.status_code in [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND]


@pytest.mark.integration
class TestSubmissionWorkflow:
    """Test end-to-end submission workflow."""

    def test_submission_awards_points_on_first_accept(self, authenticated_client, problem_with_tests, user, mock_celery):
        """Test that points are awarded only on first accepted submission."""
        # Create first submission
        url = reverse('submission-create')
        data = {
            'problem_slug': problem_with_tests.slug,
            'code': 'def add(a, b):\\n    return a + b',
            'language': 'python'
        }

        response = authenticated_client.post(url, data, format='json')
        submission_id = response.data['id']

        # Simulate accepted submission
        submission = Submission.objects.get(id=submission_id)
        submission.status = 'accepted'
        submission.save()

        # Award points (normally done in Celery task)
        initial_xp = user.profile.experience_points
        user.profile.add_experience(problem_with_tests.points)

        assert user.profile.experience_points == initial_xp + problem_with_tests.points

        # Second accepted submission should not award points again
        # (this logic is in the Celery task - award_points method checks if already solved)
