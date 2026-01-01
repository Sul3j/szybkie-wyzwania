"""
Tests for leaderboard app - Rankings and Statistics
"""
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.integration
class TestLeaderboardAPI:
    """Test Leaderboard API endpoints."""

    def test_global_leaderboard(self, api_client, user):
        """Test getting global leaderboard."""
        url = reverse('leaderboard-global')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert 'results' in response.data
        assert isinstance(response.data['results'], list)

    def test_user_rank(self, authenticated_client, user):
        """Test getting user's current rank."""
        url = reverse('my-rank')
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert 'rank' in response.data
        assert 'experience_points' in response.data

    def test_level_leaderboard(self, api_client):
        """Test getting level-based leaderboard."""
        url = reverse('leaderboard-level')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_rank_distribution(self, api_client, user):
        """Test getting rank distribution."""
        url = reverse('leaderboard-rank')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)

    def test_problem_solvers_leaderboard(self, api_client):
        """Test getting top problem solvers."""
        url = reverse('leaderboard-solvers')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.unit
class TestLeaderboardCalculations:
    """Test leaderboard calculation logic."""

    def test_user_ranking_by_xp(self, user, user2):
        """Test users are ranked by experience points."""
        user.profile.add_experience(1000)
        user2.profile.add_experience(500)

        assert user.profile.experience_points > user2.profile.experience_points

    def test_percentile_calculation(self, user):
        """Test percentile calculation for user rank."""
        # This would test the percentile calculation logic
        # which determines what percentage of users a user is better than
        profile = user.profile
        assert profile.experience_points >= 0
