from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.filter(_id__isnull=False).delete()
        Team.objects.filter(_id__isnull=False).delete()
        Activity.objects.filter(_id__isnull=False).delete()
        Leaderboard.objects.filter(_id__isnull=False).delete()
        Workout.objects.filter(_id__isnull=False).delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(*users[:3])
        team2.members.add(*users[3:])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=60, date='2025-04-08'),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=120, date='2025-04-07'),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=90, date='2025-04-06'),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=30, date='2025-04-05'),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team1, points=300),
            Leaderboard(_id=ObjectId(), team=team2, points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))