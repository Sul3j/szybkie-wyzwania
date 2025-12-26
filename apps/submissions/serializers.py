from rest_framework import serializers
from .models import Submission
from apps.problems.models import Problem


class SubmissionListSerializer(serializers.ModelSerializer):

    problem_title = serializers.CharField(source='problem.title', read_only=True)
    problem_slug = serializers.CharField(source='problem.slug', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    passed_tests = serializers.IntegerField(read_only=True)
    total_tests = serializers.IntegerField(read_only=True)

    class Meta:
        model = Submission
        fields = [
            'id', 'problem_title', 'problem_slug', 'username',
            'language', 'status', 'execution_time', 'memory_used',
            'passed_tests', 'total_tests', 'points_awarded',
            'submitted_at', 'evaluated_at'
        ]
        read_only_fields = fields


class SubmissionDetailSerializer(serializers.ModelSerializer):

    problem_title = serializers.CharField(source='problem.title', read_only=True)
    problem_slug = serializers.CharField(source='problem.slug', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    passed_tests = serializers.IntegerField(read_only=True)
    total_tests = serializers.IntegerField(read_only=True)

    class Meta:
        model = Submission
        fields = [
            'id', 'problem_title', 'problem_slug', 'username',
            'code', 'language', 'status', 'test_results',
            'execution_time', 'memory_used', 'error_message',
            'passed_tests', 'total_tests', 'points_awarded',
            'submitted_at', 'evaluated_at'
        ]
        read_only_fields = fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')

        if request and not (
            request.user == instance.user or request.user.is_staff
        ):
            data.pop('code', None)

        return data


class SubmissionCreateSerializer(serializers.ModelSerializer):

    problem_slug = serializers.SlugField(write_only=True)

    class Meta:
        model = Submission
        fields = ['problem_slug', 'code', 'language']

    def validate_problem_slug(self, value):
        try:
            Problem.objects.get(slug=value)
        except Problem.DoesNotExist:
            raise serializers.ValidationError("Problem not found.")
        return value

    def validate(self, attrs):
        problem = Problem.objects.get(slug=attrs['problem_slug'])
        language = attrs['language']

        if language not in problem.supported_languages_list:
            raise serializers.ValidationError({
                'language': f"Language '{language}' is not supported for this problem."
            })

        return attrs

    def create(self, validated_data):
        problem_slug = validated_data.pop('problem_slug')
        problem = Problem.objects.get(slug=problem_slug)

        submission = Submission.objects.create(
            problem=problem,
            user=self.context['request'].user,
            **validated_data
        )

        return submission


class SubmissionStatsSerializer(serializers.Serializer):

    total_submissions = serializers.IntegerField()
    accepted_submissions = serializers.IntegerField()
    acceptance_rate = serializers.FloatField()
    status_distribution = serializers.DictField()
    language_distribution = serializers.DictField()
