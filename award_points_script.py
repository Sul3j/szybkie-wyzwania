#!/usr/bin/env python
"""Script to award points for existing accepted submissions."""

from apps.submissions.models import Submission

# Znajdź wszystkie zaakceptowane submissions, które nie mają przydzielonych punktów
accepted_submissions = (
    Submission.objects.filter(status="accepted", points_awarded=0)
    .select_related("user", "problem")
    .order_by("submitted_at")
)

print(
    f"Znaleziono {accepted_submissions.count()} zaakceptowanych submissions bez punktów\n"
)

# Dla każdego użytkownika, przydziel punkty za pierwsze zaakceptowane rozwiązanie każdego zadania
users_awarded = {}
for submission in accepted_submissions:
    user_id = submission.user.id
    problem_id = submission.problem.id

    # Sprawdź czy ten użytkownik już dostał punkty za to zadanie (w tej sesji)
    key = f"{user_id}_{problem_id}"
    if key not in users_awarded:
        # Przyznaj punkty
        submission.award_points()
        users_awarded[key] = True
        print(
            f"✓ Przyznano {submission.points_awarded} punktów użytkownikowi {submission.user.username} za zadanie '{submission.problem.title}'"
        )

print("\n--- Profile użytkowników po aktualizacji ---")
from django.contrib.auth.models import User

for user in User.objects.all():
    profile = user.profile
    profile.refresh_from_db()
    print(
        f"{user.username}: {profile.experience_points} punktów, poziom {profile.level}, ranga {profile.rank}"
    )
