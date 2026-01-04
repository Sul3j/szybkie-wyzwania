from django.contrib import admin

from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "problem",
        "language",
        "status",
        "execution_time",
        "memory_used",
        "points_awarded",
        "is_public",
        "submitted_at",
    ]
    list_filter = ["status", "language", "is_public", "submitted_at"]
    search_fields = ["user__username", "problem__title"]
    readonly_fields = [
        "submitted_at",
        "evaluated_at",
        "published_at",
        "execution_time",
        "memory_used",
        "test_results",
        "points_awarded",
    ]
    date_hierarchy = "submitted_at"

    fieldsets = (
        ("Submission Info", {"fields": ("user", "problem", "language", "code")}),
        ("Results", {"fields": ("status", "test_results", "error_message")}),
        ("Metrics", {"fields": ("execution_time", "memory_used", "points_awarded")}),
        (
            "Sharing",
            {
                "fields": ("is_public", "solution_description", "published_at"),
                "classes": ("collapse",),
            },
        ),
        ("Timestamps", {"fields": ("submitted_at", "evaluated_at")}),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff
