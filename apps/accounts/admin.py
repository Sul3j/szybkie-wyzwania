from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"
    readonly_fields = ["experience_points", "level", "rank", "created_at", "updated_at"]


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "get_level",
        "get_rank",
    ]
    list_select_related = ["profile"]

    def get_level(self, instance):
        return instance.profile.level

    get_level.short_description = "Level"

    def get_rank(self, instance):
        return instance.profile.rank

    get_rank.short_description = "Rank"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "level",
        "rank",
        "experience_points",
        "solved_count",
        "created_at",
    ]
    list_filter = ["rank", "level", "created_at"]
    search_fields = ["user__username", "user__email"]
    readonly_fields = [
        "experience_points",
        "level",
        "rank",
        "created_at",
        "updated_at",
        "solved_count",
        "total_submissions",
        "acceptance_rate",
    ]
    fieldsets = (
        ("User Information", {"fields": ("user",)}),
        ("Gamification", {"fields": ("experience_points", "level", "rank")}),
        (
            "Statistics",
            {"fields": ("solved_count", "total_submissions", "acceptance_rate")},
        ),
        ("Profile Details", {"fields": ("bio", "avatar")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    def solved_count(self, obj):
        return obj.solved_count

    solved_count.short_description = "Solved Problems"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
