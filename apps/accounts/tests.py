"""
Tests for accounts app - Authentication, User Profiles, XP/Level System
"""

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from apps.accounts.models import UserProfile

User = get_user_model()


# ============================================================================
# MODEL TESTS
# ============================================================================


@pytest.mark.unit
class TestUserProfileModel:
    """Test UserProfile model methods and properties."""

    def test_profile_created_on_user_creation(self, user):
        """Test that profile is automatically created when user is created."""
        assert hasattr(user, "profile")
        assert isinstance(user.profile, UserProfile)
        assert user.profile.experience_points == 0
        assert user.profile.level == 1
        assert user.profile.rank == "Bronze"

    def test_add_experience_levels_up(self, user):
        """Test adding experience updates level correctly."""
        profile = user.profile

        # Add 150 XP (should reach level 2 at 100 XP)
        profile.add_experience(150)
        assert profile.experience_points == 150
        assert profile.level == 2

        # Add more to reach level 3 (threshold at 300)
        profile.add_experience(200)
        assert profile.experience_points == 350
        assert profile.level == 3

    def test_add_experience_updates_rank(self, user):
        """Test that rank updates with level progression."""
        profile = user.profile

        # Start at Bronze (level 1)
        assert profile.rank == "Bronze"

        # Level up to 5 (Silver rank - 1000 XP)
        profile.add_experience(1000)
        assert profile.level == 5
        assert profile.rank == "Silver"

        # Level up to Gold rank (5000 XP)
        profile.add_experience(4000)
        assert profile.experience_points == 5000
        assert profile.rank == "Gold"

        # Level up to Platinum rank (10000 XP)
        profile.add_experience(5000)
        assert profile.experience_points == 10000
        assert profile.rank == "Platinum"

    def test_increment_submissions(self, user):
        """Test incrementing submission counters."""
        profile = user.profile

        profile.increment_submissions(True)
        assert profile.total_submissions == 1
        assert profile.accepted_submissions == 1

        profile.increment_submissions(False)
        assert profile.total_submissions == 2
        assert profile.accepted_submissions == 1

    def test_acceptance_rate(self, user):
        """Test acceptance rate calculation."""
        profile = user.profile

        # No submissions yet
        assert profile.acceptance_rate == 0.0

        # 1 accepted out of 2
        profile.increment_submissions(True)
        profile.increment_submissions(False)
        assert profile.acceptance_rate == 50.0

        # 2 accepted out of 4
        profile.increment_submissions(True)
        profile.increment_submissions(False)
        assert profile.acceptance_rate == 50.0

    def test_string_representation(self, user):
        """Test __str__ method."""
        assert str(user.profile) == f"{user.username}'s Profile"


# ============================================================================
# API TESTS - Authentication
# ============================================================================


@pytest.mark.integration
class TestAuthenticationAPI:
    """Test authentication endpoints."""

    def test_user_registration(self, api_client):
        """Test user registration creates user and profile."""
        url = reverse("register")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "strongpass123",
            "password2": "strongpass123",
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username="newuser").exists()

        user = User.objects.get(username="newuser")
        assert hasattr(user, "profile")
        assert user.profile.experience_points == 0

    def test_registration_password_mismatch(self, api_client):
        """Test registration fails with mismatched passwords."""
        url = reverse("register")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "strongpass123",
            "password2": "differentpass",
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not User.objects.filter(username="newuser").exists()

    def test_registration_duplicate_username(self, api_client, user):
        """Test registration fails with duplicate username."""
        url = reverse("register")
        data = {
            "username": user.username,
            "email": "different@example.com",
            "password": "strongpass123",
            "password2": "strongpass123",
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_login_success(self, api_client, user):
        """Test successful login returns JWT tokens."""
        url = reverse("login")
        data = {"username": "testuser", "password": "testpass123"}

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data
        assert "user" in response.data
        assert response.data["user"]["username"] == "testuser"

    def test_login_invalid_credentials(self, api_client, user):
        """Test login fails with wrong password."""
        url = reverse("login")
        data = {"username": "testuser", "password": "wrongpassword"}

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_token_refresh(self, api_client, user):
        """Test token refresh endpoint."""
        # First login to get refresh token
        login_url = reverse("login")
        login_data = {"username": "testuser", "password": "testpass123"}
        login_response = api_client.post(login_url, login_data)
        refresh_token = login_response.data["refresh"]

        # Refresh token
        refresh_url = reverse("token_refresh")
        refresh_data = {"refresh": refresh_token}

        response = api_client.post(refresh_url, refresh_data)

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data


# ============================================================================
# API TESTS - Profile Management
# ============================================================================


@pytest.mark.integration
class TestProfileAPI:
    """Test profile management endpoints."""

    def test_get_current_user_profile(self, authenticated_client, user):
        """Test getting current user's profile."""
        url = reverse("user-profile")

        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == user.username
        assert "experience_points" in response.data
        assert "level" in response.data
        assert "rank" in response.data

    def test_update_profile(self, authenticated_client, user):
        """Test updating user profile."""
        url = reverse("user-profile")
        data = {"bio": "I love coding!", "github_url": "https://github.com/testuser"}

        response = authenticated_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        user.profile.refresh_from_db()
        assert user.profile.bio == "I love coding!"
        assert user.profile.github_url == "https://github.com/testuser"

    def test_get_profile_unauthenticated(self, api_client):
        """Test getting profile fails when not authenticated."""
        url = reverse("user-profile")

        response = api_client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_public_profile(self, api_client, user):
        """Test viewing public user profile."""
        url = reverse("user-public-profile", kwargs={"username": user.username})

        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == user.username
        assert "email" not in response.data  # Email should be private

    def test_change_password(self, authenticated_client, user):
        """Test password change."""
        url = reverse("change-password")
        data = {"old_password": "testpass123", "new_password": "newpass123"}

        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_200_OK

        # Verify new password works
        user.refresh_from_db()
        assert user.check_password("newpass123")

    def test_change_password_wrong_old_password(self, authenticated_client):
        """Test password change fails with wrong old password."""
        url = reverse("change-password")
        data = {"old_password": "wrongpass", "new_password": "newpass123"}

        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


# ============================================================================
# INTEGRATION TESTS - XP and Level System
# ============================================================================


@pytest.mark.integration
class TestXPLevelSystem:
    """Test XP and leveling system integration."""

    def test_full_level_progression(self, user):
        """Test complete level progression from 1 to max."""
        profile = user.profile

        # Test each level threshold
        thresholds = {
            1: 0,
            2: 100,
            3: 300,
            4: 600,
            5: 1000,
            6: 1500,
        }

        for level, xp_needed in thresholds.items():
            if xp_needed > 0:
                profile.add_experience(xp_needed - profile.experience_points + 1)
            assert profile.level >= level

    def test_rank_progression(self, user):
        """Test rank changes with levels."""
        profile = user.profile

        # Bronze (0 XP)
        assert profile.rank == "Bronze"

        # Silver (1000 XP)
        profile.add_experience(1000)
        assert profile.rank == "Silver"

        # Gold (5000 XP)
        profile.add_experience(4000)
        assert profile.rank == "Gold"

        # Platinum (10000 XP)
        profile.add_experience(5000)
        assert profile.rank == "Platinum"

    def test_xp_never_decreases(self, user):
        """Test that XP never decreases."""
        profile = user.profile

        profile.add_experience(500)
        assert profile.experience_points == 500

        # Adding more XP
        profile.add_experience(300)
        assert profile.experience_points == 800

        # XP should never go down
        profile.add_experience(0)
        assert profile.experience_points == 800
