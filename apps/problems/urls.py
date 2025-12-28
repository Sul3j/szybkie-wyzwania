from django.urls import path
from .views import (
    ProblemListView,
    ProblemDetailView,
    ProblemCreateView,
    ProblemUpdateView,
    ProblemDeleteView,
    ProblemTagListView,
    ProblemStatsView,
    UserProblemStatsView,
    RandomProblemView,
)

app_name = 'problems'

urlpatterns = [
    # Problem CRUD
    path('', ProblemListView.as_view(), name='problem-list'),
    path('create/', ProblemCreateView.as_view(), name='problem-create'),
    path('<slug:slug>/', ProblemDetailView.as_view(), name='problem-detail'),
    path('<slug:slug>/update/', ProblemUpdateView.as_view(), name='problem-update'),
    path('<slug:slug>/delete/', ProblemDeleteView.as_view(), name='problem-delete'),

    # Tags
    path('tags/', ProblemTagListView.as_view(), name='tag-list'),

    # Statistics
    path('stats/overall/', ProblemStatsView.as_view(), name='problem-stats'),
    path('stats/user/', UserProblemStatsView.as_view(), name='user-problem-stats'),

    # Random problem
    path('random/', RandomProblemView.as_view(), name='random-problem'),
]
