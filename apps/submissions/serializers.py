from rest_framework import serializers

from apps.problems.models import Problem

from .models import Submission


class SubmissionListSerializer(serializers.ModelSerializer):

    problem_title = serializers.CharField(source="problem.title", read_only=True)
    problem_slug = serializers.CharField(source="problem.slug", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    passed_tests = serializers.IntegerField(read_only=True)
    total_tests = serializers.IntegerField(read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "problem_title",
            "problem_slug",
            "username",
            "language",
            "status",
            "execution_time",
            "memory_used",
            "passed_tests",
            "total_tests",
            "points_awarded",
            "submitted_at",
            "evaluated_at",
        ]
        read_only_fields = fields


class SubmissionDetailSerializer(serializers.ModelSerializer):

    problem_title = serializers.CharField(source="problem.title", read_only=True)
    problem_slug = serializers.CharField(source="problem.slug", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    passed_tests = serializers.IntegerField(read_only=True)
    total_tests = serializers.IntegerField(read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "problem_title",
            "problem_slug",
            "username",
            "code",
            "language",
            "status",
            "test_results",
            "execution_time",
            "memory_used",
            "error_message",
            "passed_tests",
            "total_tests",
            "points_awarded",
            "submitted_at",
            "evaluated_at",
        ]
        read_only_fields = fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        if request and not (request.user == instance.user or request.user.is_staff):
            data.pop("code", None)

        return data


class SubmissionCreateSerializer(serializers.ModelSerializer):

    problem_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = Submission
        fields = ["problem_slug", "code", "language"]

    def validate_problem_slug(self, value):
        try:
            Problem.objects.get(slug=value)
        except Problem.DoesNotExist:
            raise serializers.ValidationError("Problem not found.")
        return value

    def validate(self, attrs):
        problem = Problem.objects.get(slug=attrs["problem_slug"])
        language = attrs["language"]

        if language not in problem.supported_languages_list:
            raise serializers.ValidationError(
                {
                    "language": f"Language '{language}' is not supported for this problem."
                }
            )

        return attrs

    def create(self, validated_data):
        problem_slug = validated_data.pop("problem_slug")
        problem = Problem.objects.get(slug=problem_slug)

        submission = Submission.objects.create(
            problem=problem, user=self.context["request"].user, **validated_data
        )

        return submission


class SubmissionStatsSerializer(serializers.Serializer):

    total_submissions = serializers.IntegerField()
    accepted_submissions = serializers.IntegerField()
    acceptance_rate = serializers.FloatField()
    status_distribution = serializers.DictField()
    language_distribution = serializers.DictField()


class PublicSolutionSerializer(serializers.ModelSerializer):
    """Serializer for publicly shared solutions - includes code."""

    username = serializers.CharField(source="user.username", read_only=True)
    problem_title = serializers.CharField(source="problem.title", read_only=True)
    problem_slug = serializers.CharField(source="problem.slug", read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "username",
            "problem_title",
            "problem_slug",
            "code",
            "language",
            "execution_time",
            "memory_used",
            "solution_description",
            "published_at",
            "submitted_at",
        ]
        read_only_fields = fields


class SubmissionPublishSerializer(serializers.ModelSerializer):
    """Serializer for publishing/unpublishing submissions."""

    solution_description = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=2000,
        help_text="Optional description of your solution approach",
    )

    class Meta:
        model = Submission
        fields = ["is_public", "solution_description"]

    def validate(self, attrs):
        submission = self.instance

        if attrs.get("is_public", False) and not submission.is_accepted:
            raise serializers.ValidationError(
                "Only accepted submissions can be published"
            )

        return attrs

    def update(self, instance, validated_data):
        is_public = validated_data.get("is_public", instance.is_public)
        description = validated_data.get("solution_description", "")

        if is_public and not instance.is_public:
            instance.publish_solution(description)
        elif is_public and instance.is_public:
            instance.solution_description = description
            instance.save(update_fields=["solution_description"])
        elif not is_public:
            instance.unpublish_solution()

        return instance
