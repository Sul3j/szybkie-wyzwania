from django.db import models
from django.contrib.auth.models import User
from apps.problems.models import Problem

class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('accepted', 'Accepted'),
        ('wrong_answer', 'Wrong Answer'),
        ('time_limit_exceeded', 'Time Limit Exceeded'),
        ('memory_limit_exceeded', 'Memory Limit Exceeded'),
        ('runtime_error', 'Runtime Error'),
        ('compilation_error', 'Compilation Error'),
        ('internal_error', 'Internal Error'),
    ]

    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('csharp', 'C#'),
        ('cpp', 'C++'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submission_set'
    )
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    code = models.TextField(help_text="User's submitted code")
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='pending'
    )

    test_results = models.JSONField(
        null=True,
        blank=True,
        help_text="Detailed test case results"
    )

    execution_time = models.IntegerField(
        null=True,
        blank=True,
        help_text="Execution time in milliseconds"
    )
    memory_used = models.IntegerField(
        null=True,
        blank=True,
        help_text="Memory used in MB"
    )

    error_message = models.TextField(
        blank=True,
        null=True,
        help_text="Error message if submission failed"
    )

    points_awarded = models.IntegerField(
        default=0,
        help_text="Points awarded for this submission"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)
    evaluated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'
        indexes = [
            models.Index(fields=['user', 'problem']),
            models.Index(fields=['status']),
            models.Index(fields=['submitted_at']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} ({self.status})"
    

    @property
    def is_accepted(self):
        return self.status == 'accepted'

    @property
    def passed_tests(self):
        if not self.test_results:
            return 0
        return sum(1 for result in self.test_results if result.get('passed', False))

    @property
    def total_tests(self):
        if not self.test_results:
            return 0
        return len(self.test_results)

    def award_points(self):
        if self.is_accepted:
            previous_accepted = Submission.objects.filter(
                user=self.user,
                problem=self.problem,
                status='accepted',
                submitted_at__lt=self.submitted_at
            ).exists()

            if not previous_accepted:
                self.points_awarded = self.problem.points

                if hasattr(self.user, 'profile'):
                    self.user.profile.add_experience(self.points_awarded)
                else:
                    from apps.accounts.models import UserProfile
                    UserProfile.objects.create(user=self.user)
                    self.user.profile.add_experience(self.points_awarded)

                self.save(update_fields=['points_awarded'])
