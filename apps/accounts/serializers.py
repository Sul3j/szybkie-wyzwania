from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    solved_count = serializers.IntegerField(read_only=True)
    total_submissions = serializers.IntegerField(read_only=True)
    acceptance_rate = serializers.FloatField(read_only=True)
    easy_solved = serializers.SerializerMethodField()
    medium_solved = serializers.SerializerMethodField()
    hard_solved = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'bio', 'github_url', 'avatar',
            'experience_points', 'level', 'rank',
            'solved_count', 'total_submissions', 'acceptance_rate',
            'easy_solved', 'medium_solved', 'hard_solved',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['experience_points', 'level', 'rank', 'created_at', 'updated_at']

    def get_easy_solved(self, obj):
        from apps.problems.models import Problem
        solved_problem_ids = obj.user.submission_set.filter(
            status='accepted'
        ).values_list('problem_id', flat=True).distinct()

        return Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='easy'
        ).count()

    def get_medium_solved(self, obj):
        from apps.problems.models import Problem
        solved_problem_ids = obj.user.submission_set.filter(
            status='accepted'
        ).values_list('problem_id', flat=True).distinct()

        return Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='medium'
        ).count()

    def get_hard_solved(self, obj):
        from apps.problems.models import Problem
        solved_problem_ids = obj.user.submission_set.filter(
            status='accepted'
        ).values_list('problem_id', flat=True).distinct()

        return Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='hard'
        ).count()


class PublicUserProfileSerializer(serializers.ModelSerializer):
    """Public profile serializer without email."""
    username = serializers.CharField(source='user.username', read_only=True)
    solved_count = serializers.IntegerField(read_only=True)
    total_submissions = serializers.IntegerField(read_only=True)
    acceptance_rate = serializers.FloatField(read_only=True)
    easy_solved = serializers.SerializerMethodField()
    medium_solved = serializers.SerializerMethodField()
    hard_solved = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'bio', 'github_url', 'avatar',
            'experience_points', 'level', 'rank',
            'solved_count', 'total_submissions', 'acceptance_rate',
            'easy_solved', 'medium_solved', 'hard_solved',
            'created_at', 'updated_at'
        ]
        read_only_fields = fields  # All fields are read-only for public view

    def get_easy_solved(self, obj):
        from apps.problems.models import Problem
        solved_problem_ids = obj.user.submission_set.filter(
            status='accepted'
        ).values_list('problem_id', flat=True).distinct()

        return Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='easy'
        ).count()

    def get_medium_solved(self, obj):
        from apps.problems.models import Problem
        solved_problem_ids = obj.user.submission_set.filter(
            status='accepted'
        ).values_list('problem_id', flat=True).distinct()

        return Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='medium'
        ).count()

    def get_hard_solved(self, obj):
        from apps.problems.models import Problem
        solved_problem_ids = obj.user.submission_set.filter(
            status='accepted'
        ).values_list('problem_id', flat=True).distinct()

        return Problem.objects.filter(
            id__in=solved_problem_ids,
            difficulty='hard'
        ).count()
    
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user