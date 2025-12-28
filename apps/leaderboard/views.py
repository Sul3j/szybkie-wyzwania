from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.db.models import Count, Q, Avg, Max
from apps.accounts.models import UserProfile
from apps.accounts.serializers import UserProfileSerializer
from apps.submissions.models import Submission


class GlobalLeaderboardView(generics.ListAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 100))
        return UserProfile.objects.select_related('user').order_by('-experience_points')[:limit]


class LevelLeaderboardView(generics.ListAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 100))
        return UserProfile.objects.select_related('user').order_by('-level', '-experience_points')[:limit]


class RankLeaderboardView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        rank_distribution = {}

        for rank in ['Beginner', 'Novice', 'Intermediate', 'Advanced', 'Expert', 'Master']:
            users = UserProfile.objects.filter(rank=rank).select_related('user')
            rank_distribution[rank] = {
                'count': users.count(),
                'top_users': UserProfileSerializer(users[:10], many=True).data
            }

        return Response(rank_distribution)


class ProblemSolversLeaderboardView(generics.ListAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 100))

        users_with_solved = []
        for profile in UserProfile.objects.select_related('user').all():
            solved_count = profile.solved_count
            if solved_count > 0:
                users_with_solved.append((profile, solved_count))

        users_with_solved.sort(key=lambda x: x[1], reverse=True)

        return [user[0] for user in users_with_solved[:limit]]


class StreakLeaderboardView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        limit = int(request.query_params.get('limit', 100))

        users = UserProfile.objects.select_related('user')[:limit]
        serializer = UserProfileSerializer(users, many=True)

        return Response({
            'message': 'Streak tracking coming soon!',
            'top_users': serializer.data
        })


class WeeklyLeaderboardView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        from datetime import datetime, timedelta

        limit = int(request.query_params.get('limit', 100))
        week_ago = datetime.now() - timedelta(days=7)

        weekly_submissions = Submission.objects.filter(
            status='accepted',
            submitted_at__gte=week_ago
        ).select_related('user', 'problem')

        user_points = {}
        for submission in weekly_submissions:
            user_id = submission.user.id
            if user_id not in user_points:
                user_points[user_id] = {
                    'user': submission.user,
                    'points': 0,
                    'problems_solved': set()
                }

            if submission.problem.id not in user_points[user_id]['problems_solved']:
                user_points[user_id]['points'] += submission.problem.points
                user_points[user_id]['problems_solved'].add(submission.problem.id)

        sorted_users = sorted(
            user_points.values(),
            key=lambda x: x['points'],
            reverse=True
        )[:limit]

        result = []
        for item in sorted_users:
            user_profile = item['user'].profile
            result.append({
                'username': item['user'].username,
                'weekly_points': item['points'],
                'problems_solved_this_week': len(item['problems_solved']),
                'total_experience': user_profile.experience_points,
                'level': user_profile.level,
                'rank': user_profile.rank
            })

        return Response(result)


class UserRankingView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = user.profile

        higher_ranked = UserProfile.objects.filter(
            experience_points__gt=profile.experience_points
        ).count()
        global_rank = higher_ranked + 1

        total_users = UserProfile.objects.count()

        percentile = round((1 - (global_rank / total_users)) * 100, 2) if total_users > 0 else 0

        return Response({
            'global_rank': global_rank,
            'total_users': total_users,
            'percentile': percentile,
            'experience_points': profile.experience_points,
            'level': profile.level,
            'rank': profile.rank,
            'solved_problems': profile.solved_count
        })
