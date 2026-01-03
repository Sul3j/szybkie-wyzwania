from django.urls import path

from .views import (ProblemCreateView, ProblemDeleteView, ProblemDetailView,
                    ProblemListView, ProblemStatsView, ProblemTagListView,
                    ProblemUpdateView, RandomProblemView, UserProblemStatsView)

urlpatterns = [
    # Random problem (must be before <slug:slug>/)
    path("random/", RandomProblemView.as_view(), name="problem-random"),
    # Problem CRUD
    path("", ProblemListView.as_view(), name="problem-list"),
    path("create/", ProblemCreateView.as_view(), name="problem-create"),
    path("<slug:slug>/", ProblemDetailView.as_view(), name="problem-detail"),
    path("<slug:slug>/update/", ProblemUpdateView.as_view(), name="problem-update"),
    path("<slug:slug>/delete/", ProblemDeleteView.as_view(), name="problem-delete"),
    # Tags
    path("tags/", ProblemTagListView.as_view(), name="tag-list"),
    # Statistics
    path("stats/overall/", ProblemStatsView.as_view(), name="problem-stats"),
    path("stats/user/", UserProblemStatsView.as_view(), name="user-problem-stats"),
]
