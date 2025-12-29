from django.shortcuts import render, get_object_or_404
from apps.problems.models import Problem


def home_view(request):
    return render(request, 'home.html')


def problems_view(request):
    return render(request, 'problems.html')


def problem_detail_view(request, slug):
    problem = get_object_or_404(Problem, slug=slug)

    context = {
        'problem': problem,
    }
    return render(request, 'problem_detail.html', context)


def leaderboard_view(request):
    return render(request, 'leaderboard.html')


def profile_view(request):
    return render(request, 'profile.html')


def register_view(request):
    return render(request, 'register.html')
