from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

def api_root(request, format=None):
    codespace_url = "https://effective-fortnight-4jpjx55x94r2qrrw-8000.app.github.dev"
    return Response({
        'users': f"{codespace_url}{reverse('user-list', request=request, format=format)}",
        'teams': f"{codespace_url}{reverse('team-list', request=request, format=format)}",
        'activities': f"{codespace_url}{reverse('activity-list', request=request, format=format)}",
        'leaderboard': f"{codespace_url}{reverse('leaderboard-list', request=request, format=format)}",
        'workouts': f"{codespace_url}{reverse('workout-list', request=request, format=format)}",
    })