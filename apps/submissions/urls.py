from django.urls import path

from .views import (AllSubmissionsView, ProblemSubmissionsView,
                    PublicSolutionsView, RecentSubmissionsView,
                    SubmissionCreateView, SubmissionDetailView,
                    SubmissionListView, SubmissionPublishView,
                    UserSubmissionStatsView)

urlpatterns = [
    # Submission CRUD
    path("", SubmissionListView.as_view(), name="submission-list"),
    path("create/", SubmissionCreateView.as_view(), name="submission-create"),
    path("<int:pk>/", SubmissionDetailView.as_view(), name="submission-detail"),
    # All submissions
    path("all/", AllSubmissionsView.as_view(), name="all-submissions"),
    path("recent/", RecentSubmissionsView.as_view(), name="recent-submissions"),
    # Problem-specific submissions
    path(
        "problem/<slug:problem_slug>/",
        ProblemSubmissionsView.as_view(),
        name="problem-submissions",
    ),
    # Public solutions
    path(
        "problem/<slug:problem_slug>/public/",
        PublicSolutionsView.as_view(),
        name="public-solutions",
    ),
    # Publish/unpublish submission
    path(
        "<int:pk>/publish/",
        SubmissionPublishView.as_view(),
        name="submission-publish",
    ),
    # Statistics
    path("stats/", UserSubmissionStatsView.as_view(), name="user-submission-stats"),
]
