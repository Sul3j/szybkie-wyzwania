from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Problem, ProblemTag
from .serializers import (
    ProblemListSerializer,
    ProblemDetailSerializer,
    ProblemCreateSerializer,
    ProblemTagSerializer,
)

class ProblemListView(generics.ListAPIView):

    serializer_class = ProblemListSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'difficulty', 'points', 'total_submissions']
    ordering = ['-created_at']

    def get_queryset(self):

        queryset = Problem.objects.all()

        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        tags = self.request.query_params.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            queryset = queryset.filter(tags__slug__in=tag_list).distinct()

        if self.request.user.is_authenticated:
            solved = self.request.query_params.get('solved')
            if solved == 'true':
                solved_problem_ids = self.request.user.submission_set.filter(
                    status='accepted'
                ).values_list('problem_id', flat=True).distinct()
                queryset = queryset.filter(id__in=solved_problem_ids)
            elif solved == 'false':
                solved_problem_ids = self.request.user.submission_set.filter(
                    status='accepted'
                ).values_list('problem_id', flat=True).distinct()
                queryset = queryset.exclude(id__in=solved_problem_ids)

        return queryset
    
class ProblemDetailView(generics.RetrieveAPIView):

    serializer_class = ProblemDetailSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Problem.objects.all()
    lookup_field = 'slug'

class ProblemCreateView(generics.CreateAPIView):

    serializer_class = ProblemCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProblemUpdateView(generics.UpdateAPIView):

    serializer_class = ProblemCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Problem.objects.all()
    lookup_field = 'slug'

class ProblemDeleteView(generics.DestroyAPIView):

    permission_classes = [permissions.IsAdminUser]
    queryset = Problem.objects.all()
    lookup_field = 'slug'

class ProblemTagListView(generics.ListAPIView):
    
    serializer_class = ProblemTagSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ProblemTag.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProblemStatsView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        from django.contrib.auth.models import User
        from apps.submissions.models import Submission

        total_problems = Problem.objects.count()
        easy_count = Problem.objects.filter(difficulty='easy').count()
        medium_count = Problem.objects.filter(difficulty='medium').count()
        hard_count = Problem.objects.filter(difficulty='hard').count()
        total_users = User.objects.count()
        total_submissions = Submission.objects.count()

        return Response({
            'total_problems': total_problems,
            'difficulty_distribution': {
                'easy': easy_count,
                'medium': medium_count,
                'hard': hard_count
            },
            'total_users': total_users,
            'total_submissions': total_submissions
        })
    

class UserProblemStatsView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        
        solved_submissions = user.submission_set.filter(status='accepted')
        solved_problem_ids = solved_submissions.values_list('problem_id', flat=True).distinct()

        solved_easy = Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='easy'
        ).count()

        solved_medium = Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='medium'
        ).count()

        solved_hard = Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='hard'
        ).count()

        return Response({
            'total_solved': len(solved_problem_ids),
            'solved_by_difficulty': {
                'easy': solved_easy,
                'medium': solved_medium,
                'hard': solved_hard
            },
            'total_submissions': user.submission_set.count(),
            'acceptance_rate': user.profile.acceptance_rate
        })
    

class RandomProblemView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):

        difficulty = request.query_params.get('difficulty')

        queryset = Problem.objects.all()

        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        problem = queryset.order_by('?').first()

        if problem:
            serializer = ProblemListSerializer(problem, context={'request': request})
            return Response(serializer.data)
        
        return Response(
            {'error': 'No problems found'},
            status=status.HTTP_404_NOT_FOUND
        )