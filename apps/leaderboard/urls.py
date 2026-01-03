from django.urls import path
from .views import (
    GlobalLeaderboardView,
    LevelLeaderboardView,
    RankLeaderboardView,
    ProblemSolversLeaderboardView,
    StreakLeaderboardView,
    WeeklyLeaderboardView,
    UserRankingView,
)

urlpatterns = [
    # Leaderboards
    path('global/', GlobalLeaderboardView.as_view(), name='leaderboard-global'),
    path('level/', LevelLeaderboardView.as_view(), name='leaderboard-level'),
    path('rank/', RankLeaderboardView.as_view(), name='leaderboard-rank'),
    path('solvers/', ProblemSolversLeaderboardView.as_view(), name='leaderboard-solvers'),
    path('streak/', StreakLeaderboardView.as_view(), name='streak-leaderboard'),
    path('weekly/', WeeklyLeaderboardView.as_view(), name='weekly-leaderboard'),

    # User ranking
    path('my-rank/', UserRankingView.as_view(), name='my-rank'),
]
