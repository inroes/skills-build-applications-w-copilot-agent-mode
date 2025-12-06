from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Eliminar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User(email='ironman@marvel.com', username='ironman', team=marvel),
            User(email='spiderman@marvel.com', username='spiderman', team=marvel),
            User(email='batman@dc.com', username='batman', team=dc),
            User(email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Crear actividades
        Activity.objects.create(user=users[0], type='run', duration=30)
        Activity.objects.create(user=users[1], type='cycle', duration=45)
        Activity.objects.create(user=users[2], type='swim', duration=60)
        Activity.objects.create(user=users[3], type='walk', duration=20)

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=80)

        # Crear workouts
        Workout.objects.create(name='Cardio Blast', description='Intenso cardio', duration=40)
        Workout.objects.create(name='Strength Builder', description='Fuerza y resistencia', duration=50)

        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de prueba.'))
