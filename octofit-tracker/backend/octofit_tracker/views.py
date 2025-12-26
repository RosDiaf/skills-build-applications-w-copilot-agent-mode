from rest_framework import viewsets
from .models import OctoUser, Team, Activity, Workout, Leaderboard
from .serializers import (
    OctoUserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer
)

class OctoUserViewSet(viewsets.ModelViewSet):
    queryset = OctoUser.objects.all()
    serializer_class = OctoUserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
