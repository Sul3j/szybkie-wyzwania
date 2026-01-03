from django.urls import path

from .views import (AllSubmissionsView, ProblemSubmissionsView,
                    RecentSubmissionsView, SubmissionCreateView,
                    SubmissionDetailView, SubmissionListView,
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
    # Statistics
    path("stats/", UserSubmissionStatsView.as_view(), name="user-submission-stats"),
]
