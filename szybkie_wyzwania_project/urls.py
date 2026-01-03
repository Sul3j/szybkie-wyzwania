from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import (home_view, leaderboard_view, problem_detail_view,
                    problems_view, profile_view, register_view)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/problems/", include("apps.problems.urls")),
    path("api/submissions/", include("apps.submissions.urls")),
    path("api/leaderboard/", include("apps.leaderboard.urls")),
    path("", home_view, name="home"),
    path("register/", register_view, name="register-page"),
    path("problems/", problems_view, name="problems-page"),
    path("problems/<slug:slug>/", problem_detail_view, name="problem-detail-page"),
    path("leaderboard/", leaderboard_view, name="leaderboard-page"),
    path("profile/", profile_view, name="profile-page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Szybkie Wyzwania Admin"
admin.site.site_title = "Szybkie Wyzwania"
admin.site.index_title = "Welcome to Szybkie Wyzwania Administration"
