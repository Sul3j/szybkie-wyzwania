from django.db.models import Count, Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.judge.tasks import evaluate_submission

from .models import Submission
from .serializers import (SubmissionCreateSerializer,
                          SubmissionDetailSerializer, SubmissionListSerializer,
                          SubmissionStatsSerializer)


class SubmissionCreateView(generics.CreateAPIView):

    serializer_class = SubmissionCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        submission = serializer.save()

        # Trigger asynchronous evaluation
        evaluate_submission.delay(submission.id)

        return Response(
            {
                "id": submission.id,
                "status": submission.status,
                "message": "Submission created and queued for evaluation.",
            },
            status=status.HTTP_201_CREATED,
        )


class SubmissionListView(generics.ListAPIView):

    serializer_class = SubmissionListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user)

        problem_slug = self.request.query_params.get("problem")
        if problem_slug:
            queryset = queryset.filter(problem__slug=problem_slug)

        status_filter = self.request.query_params.get("status")
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        language = self.request.query_params.get("language")
        if language:
            queryset = queryset.filter(language=language)

        return queryset.select_related("problem", "user")


class SubmissionDetailView(generics.RetrieveAPIView):

    serializer_class = SubmissionDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Submission.objects.all()
        return Submission.objects.filter(user=self.request.user)


class AllSubmissionsView(generics.ListAPIView):

    serializer_class = SubmissionListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Submission.objects.filter(status="accepted").select_related(
            "problem", "user"
        )

        # Filter by problem
        problem_slug = self.request.query_params.get("problem")
        if problem_slug:
            queryset = queryset.filter(problem__slug=problem_slug)

        return queryset.order_by("-submitted_at")


class UserSubmissionStatsView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        submissions = Submission.objects.filter(user=user)

        total_submissions = submissions.count()
        accepted_submissions = submissions.filter(status="accepted").count()
        acceptance_rate = (
            round((accepted_submissions / total_submissions) * 100, 2)
            if total_submissions > 0
            else 0
        )

        status_distribution = dict(
            submissions.values("status")
            .annotate(count=Count("status"))
            .values_list("status", "count")
        )

        language_distribution = dict(
            submissions.values("language")
            .annotate(count=Count("language"))
            .values_list("language", "count")
        )

        serializer = SubmissionStatsSerializer(
            data={
                "total_submissions": total_submissions,
                "accepted_submissions": accepted_submissions,
                "acceptance_rate": acceptance_rate,
                "status_distribution": status_distribution,
                "language_distribution": language_distribution,
            }
        )

        serializer.is_valid()
        return Response(serializer.data)


class RecentSubmissionsView(generics.ListAPIView):

    serializer_class = SubmissionListSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Submission.objects.all().select_related("problem", "user")[:50]


class ProblemSubmissionsView(generics.ListAPIView):

    serializer_class = SubmissionListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        problem_slug = self.kwargs.get("problem_slug")
        return (
            Submission.objects.filter(problem__slug=problem_slug, status="accepted")
            .select_related("problem", "user")
            .order_by("execution_time")
        )
