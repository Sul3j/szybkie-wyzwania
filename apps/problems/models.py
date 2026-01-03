from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Problem(models.Model):

    DIFFICULTY_CHOICES = [
        ("easy", "Łatwe"),
        ("medium", "Średnie"),
        ("hard", "Trudne"),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(
        help_text="Problem description with examples and constraints"
    )
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY_CHOICES, default="easy"
    )
    points = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(1000)],
        help_text="Experience points awarded for solving",
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_problems"
    )

    languages = models.CharField(
        max_length=100,
        default="python,javascript,csharp,cpp",
        help_text="Comma-separated list of supported languages",
    )

    time_limit = models.IntegerField(
        default=2000, help_text="Time limit in milliseconds"
    )

    memory_limit = models.IntegerField(default=128, help_text="Memory limit in MB")

    function_signature_python = models.TextField(
        blank=True, null=True, help_text="Python function signature/template"
    )
    function_signature_javascript = models.TextField(
        blank=True, null=True, help_text="JavaScript function signature/template"
    )
    function_signature_csharp = models.TextField(
        blank=True, null=True, help_text="C# function signature/template"
    )
    function_signature_cpp = models.TextField(
        blank=True, null=True, help_text="C++ function signature/template"
    )

    total_submissions = models.IntegerField(default=0)
    accepted_submissions = models.IntegerField(default=0)

    @property
    def acceptance_rate(self):
        if self.total_submissions == 0:
            return 0
        return round((self.accepted_submissions / self.total_submissions) * 100, 2)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Problem"
        verbose_name_plural = "Problems"
        indexes = [
            models.Index(fields=["difficulty"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.difficulty})"

    @property
    def supported_languages_list(self):
        return [lang.strip() for lang in self.languages.split(",")]

    def get_function_signature(self, language):
        signature_map = {
            "python": self.function_signature_python,
            "javascript": self.function_signature_javascript,
            "csharp": self.function_signature_csharp,
            "cpp": self.function_signature_cpp,
        }
        return signature_map.get(language, "")

    def increment_submissions(self, accepted=False):
        self.total_submissions += 1
        if accepted:
            self.accepted_submissions += 1
        self.save(update_fields=["total_submissions", "accepted_submissions"])


class TestCase(models.Model):
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name="test_cases"
    )
    input_data = models.TextField(
        help_text="Input data for the test case (can be JSON)"
    )
    expected_output = models.TextField(help_text="Expected output for the test case")
    is_hidden = models.BooleanField(
        default=False, help_text="Hidden test cases are not shown to users"
    )
    order = models.IntegerField(default=0, help_text="Order of test case execution")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Test Case"
        verbose_name_plural = "Test Cases"

    def __str__(self):
        visibility = "Hidden" if self.is_hidden else "Visible"
        return f"{self.problem.title} - Test Case #{self.order} ({visibility})"


class ProblemTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True)
    problems = models.ManyToManyField(Problem, related_name="tags", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

    @property
    def problem_count(self):
        return self.problems.count()


class ProblemHint(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="hints")
    order = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Hint"
        verbose_name_plural = "Hints"

    def __str__(self):
        return f"{self.problem.title} - Hint #{self.order}"
