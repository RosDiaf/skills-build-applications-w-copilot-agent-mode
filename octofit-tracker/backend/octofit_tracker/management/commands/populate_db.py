from django.core.management.base import BaseCommand

from octofit_tracker.models import Team, OctoUser, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        OctoUser.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = OctoUser.objects.create(username='ironman', email='ironman@marvel.com', team_id=marvel.id)
        captain = OctoUser.objects.create(username='captain', email='captain@marvel.com', team_id=marvel.id)
        batman = OctoUser.objects.create(username='batman', email='batman@dc.com', team_id=dc.id)
        superman = OctoUser.objects.create(username='superman', email='superman@dc.com', team_id=dc.id)

        # Create Activities
        Activity.objects.create(user_id=ironman.id, type='run', duration=30, distance=5)
        Activity.objects.create(user_id=captain.id, type='cycle', duration=60, distance=20)
        Activity.objects.create(user_id=batman.id, type='swim', duration=45, distance=2)
        Activity.objects.create(user_id=superman.id, type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', team_id=marvel.id)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', team_id=dc.id)

        # Create Leaderboard
        Leaderboard.objects.create(user_id=ironman.id, points=100)
        Leaderboard.objects.create(user_id=batman.id, points=120)
        Leaderboard.objects.create(user_id=superman.id, points=110)
        Leaderboard.objects.create(user_id=captain.id, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
