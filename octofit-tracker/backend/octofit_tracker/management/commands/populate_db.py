from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Peter Parker', email='peter@marvel.com', team=marvel),
            User(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User(name='Clark Kent', email='clark@dc.com', team=dc),
            User(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User(name='Diana Prince', email='diana@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30)
        Activity.objects.create(user=users[1], type='Cycling', duration=45)
        Activity.objects.create(user=users[3], type='Swimming', duration=60)

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        workout2 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        workout1.suggested_for.set([users[0], users[1], users[3]])
        workout2.suggested_for.set([users[2], users[4], users[5]])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
