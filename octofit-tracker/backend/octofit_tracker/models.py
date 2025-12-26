from djongo import models
import uuid

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class OctoUser(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=36, null=True, blank=True)

class Activity(models.Model):
    user_id = models.CharField(max_length=36)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team_id = models.CharField(max_length=36, null=True, blank=True)

class Leaderboard(models.Model):
    user_id = models.CharField(max_length=36)
    points = models.IntegerField()

