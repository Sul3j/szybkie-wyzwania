from django.contrib import admin
from django.utils.text import slugify

from .models import Problem, ProblemHint, ProblemTag, TestCase


class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1
    fields = ["input_data", "expected_output", "is_hidden", "order"]


class ProblemHintInline(admin.TabularInline):
    model = ProblemHint
    extra = 1
    fields = ["order", "content"]


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "difficulty",
        "points",
        "acceptance_rate",
        "total_submissions",
        "created_by",
        "created_at",
    ]
    list_filter = ["difficulty", "created_at", "tags"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = [
        "total_submissions",
        "accepted_submissions",
        "acceptance_rate",
        "created_at",
        "updated_at",
    ]
    inlines = [TestCaseInline, ProblemHintInline]
    filter_horizontal = ["tags"]

    fieldsets = (
        (
            "Basic Information",
            {"fields": ("title", "slug", "description", "difficulty", "points")},
        ),
        (
            "Language Settings",
            {
                "fields": (
                    "languages",
                    "function_signature_python",
                    "function_signature_javascript",
                    "function_signature_csharp",
                    "function_signature_cpp",
                )
            },
        ),
        ("Execution Limits", {"fields": ("time_limit", "memory_limit")}),
        (
            "Statistics",
            {
                "fields": (
                    "total_submissions",
                    "accepted_submissions",
                    "acceptance_rate",
                )
            },
        ),
        ("Metadata", {"fields": ("created_by", "created_at", "updated_at")}),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ["problem", "order", "is_hidden", "created_at"]
    list_filter = ["is_hidden", "problem__difficulty"]
    search_fields = ["problem__title"]
    ordering = ["problem", "order"]


@admin.register(ProblemTag)
class ProblemTagAdmin(admin.ModelAdmin):
    list_display = ["name", "problem_count", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ["problems"]

    def problem_count(self, obj):
        return obj.problem_count

    problem_count.short_description = "Problems"


@admin.register(ProblemHint)
class ProblemHintAdmin(admin.ModelAdmin):
    list_display = ["problem", "order", "content_preview", "created_at"]
    list_filter = ["problem__difficulty"]
    search_fields = ["problem__title", "content"]
    ordering = ["problem", "order"]

    def content_preview(self, obj):
        return obj.content[:100] + "..." if len(obj.content) > 100 else obj.content

    content_preview.short_description = "Content Preview"
