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

app_name = 'leaderboard'

urlpatterns = [
    # Leaderboards
    path('global/', GlobalLeaderboardView.as_view(), name='global-leaderboard'),
    path('level/', LevelLeaderboardView.as_view(), name='level-leaderboard'),
    path('rank/', RankLeaderboardView.as_view(), name='rank-leaderboard'),
    path('solvers/', ProblemSolversLeaderboardView.as_view(), name='solvers-leaderboard'),
    path('streak/', StreakLeaderboardView.as_view(), name='streak-leaderboard'),
    path('weekly/', WeeklyLeaderboardView.as_view(), name='weekly-leaderboard'),

    # User ranking
    path('my-rank/', UserRankingView.as_view(), name='user-ranking'),
]
