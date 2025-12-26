from django.test import TestCase
from .models import OctoUser, Team, Activity, Workout, Leaderboard

class OctoUserModelTest(TestCase):
    def test_create_user(self):
        user = OctoUser.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_id='1', type='run', duration=30, distance=5.0)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.distance, 5.0)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Morning Cardio', description='Cardio session')
        self.assertEqual(workout.name, 'Morning Cardio')
        self.assertEqual(workout.description, 'Cardio session')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user_id='1', points=100)
        self.assertEqual(leaderboard.user_id, '1')
        self.assertEqual(leaderboard.points, 100)
