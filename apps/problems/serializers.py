from rest_framework import serializers
from .models import Problem, TestCase, ProblemTag, ProblemHint

class TestCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCase
        fields = ['id', 'input_data', 'expected_output', 'is_hidden', 'order']
        read_only_fields = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.is_hidden and not self.context.get('show_hidden', False):
            data['expected_output'] = 'Hidden'
        return data
    
class ProblemHintSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProblemHint
        fields = ['id', 'order', 'content']
        read_only_fields = ['id']


class ProblemTagSerializer(serializers.ModelSerializer):

    problem_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProblemTag
        fields = ['id', 'name', 'slug', 'description', 'problem_count']
        read_only_fields = ['id', 'slug']


class ProblemListSerializer(serializers.ModelSerializer):

    created_by = serializers.CharField(source='created_by.username', read_only=True)
    acceptance_rate = serializers.FloatField(read_only=True)
    tags = ProblemTagSerializer(many=True, read_only=True)
    is_solved = serializers.SerializerMethodField()
    solved_language = serializers.SerializerMethodField()
    supported_languages_list = serializers.ListField(read_only=True)

    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'slug', 'difficulty', 'points',
            'acceptance_rate', 'total_submissions', 'created_by',
            'created_at', 'tags', 'is_solved', 'solved_language',
            'languages', 'supported_languages_list'
        ]
        read_only_fields = ['id', 'slug', 'total_submissions', 'accepted_submissions']

    def get_is_solved(self, obj):

        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.submissions.filter(
                user=request.user,
                status='accepted'
            ).exists()
        return False
    
    def get_solved_language(self, obj):

        request = self.context.get('request')
        if request and request.user.is_authenticated:
            
            accepted_submission = obj.submissions.filter(
                user=request.user,
                status='accepted'
            ).values_list('language', flat=True).distinct()

            language_list = list(accepted_submission)

            return language_list if language_list else None
        return None
    

class ProblemDetailSerializer(serializers.ModelSerializer):

    created_by = serializers.CharField(source='created_by.username', read_only=True)
    acceptance_rate = serializers.FloatField(read_only=True)
    supported_languages_list = serializers.ListField(read_only=True)
    test_cases = serializers.SerializerMethodField()
    hints = ProblemHintSerializer(many=True, read_only=True)
    tags = ProblemTagSerializer(many=True, read_only=True)
    is_solved = serializers.SerializerMethodField()
    solved_language = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'slug', 'description', 'difficulty', 'points',
            'time_limit', 'memory_limit', 'languages', 'supported_languages_list',
            'function_signature_python', 'function_signature_javascript',
            'function_signature_csharp', 'function_signature_cpp', 'acceptance_rate',
            'total_submissions', 'accepted_submissions',
            'created_by', 'created_at', 'updated_at',
            'test_cases', 'hints', 'tags', 'is_solved', 'solved_language'
        ]
        read_only_fields = [
            'id', 'slug', 'total_submissions', 'accepted_submissions',
            'created_at', 'updated_at'
        ]

    def get_test_cases(self, obj):
        request = self.context.get('request')
        if request and request.user.is_staff:
            test_cases = obj.test_cases.all()
            return TestCaseSerializer(
                test_cases,
                many=True,
                context={'show_hidden': True}
            ).data
        else:
            test_cases = obj.test_cases.filter(is_hidden=False)
            return TestCaseSerializer(test_cases, many=True).data

    def get_is_solved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.submissions.filter(
                user=request.user,
                status='accepted'
            ).exists()
        return False

    def get_solved_language(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            accepted_submissions = obj.submissions.filter(
                user=request.user,
                status='accepted'
            ).values_list('language', flat=True).distinct()

            languages_list = list(accepted_submissions)

            return languages_list if languages_list else None
        return None
    

class ProblemCreateSerializer(serializers.ModelSerializer):

    test_cases = TestCaseSerializer(many=True, write_only=True)
    hints = ProblemHintSerializer(many=True, required=False, write_only=True)
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        write_only=True
    )

    class Meta:
        model = Problem
        fields = [
            'title', 'description', 'difficulty', 'points',
            'time_limit', 'memory_limit', 'languages',
            'function_signature_python', 'function_signature_javascript',
            'function_signature_csharp', 'function_signature_cpp', 'test_cases', 'hints', 'tag_ids'
        ]

    def create(self, validated_data):
        test_cases_data = validated_data.pop('test_cases')
        hints_data = validated_data.pop('hints', [])
        tag_ids = validated_data.pop('tag_ids', [])

        problem = Problem.objects.create(**validated_data)

        for test_case_data in test_cases_data:
            TestCase.objects.create(problem=problem, **test_case_data)

        for hint_data in hints_data:
            ProblemHint.objects.create(problem=problem, **hint_data)

        if tag_ids:
            tags = ProblemTag.objects.filter(id__in=tag_ids)
            problem.tags.set(tags)

        return problem
    

class ProblemStatsSerializer(serializers.ModelSerializer):

    acceptance_rate = serializers.FloatField(read_only=True)

    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'difficulty', 
            'total_submissions', 'accepted_submissions', 'acceptance_rate'
        ]
        read_only_fields = fields