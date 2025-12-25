from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection

from django.contrib.auth import get_user_model

# Sample data
USERS = [
    {"email": "ironman@marvel.com", "username": "ironman", "first_name": "Tony", "last_name": "Stark"},
    {"email": "spiderman@marvel.com", "username": "spiderman", "first_name": "Peter", "last_name": "Parker"},
    {"email": "batman@dc.com", "username": "batman", "first_name": "Bruce", "last_name": "Wayne"},
    {"email": "wonderwoman@dc.com", "username": "wonderwoman", "first_name": "Diana", "last_name": "Prince"},
]

TEAMS = [
    {"name": "Marvel", "members": ["ironman", "spiderman"]},
    {"name": "DC", "members": ["batman", "wonderwoman"]},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "Running", "duration": 30},
    {"user": "spiderman", "activity": "Cycling", "duration": 45},
    {"user": "batman", "activity": "Swimming", "duration": 60},
    {"user": "wonderwoman", "activity": "Yoga", "duration": 50},
]

LEADERBOARD = [
    {"user": "ironman", "points": 100},
    {"user": "spiderman", "points": 90},
    {"user": "batman", "points": 95},
    {"user": "wonderwoman", "points": 110},
]

WORKOUTS = [
    {"name": "Full Body", "suggested_for": ["ironman", "batman"]},
    {"name": "Cardio Blast", "suggested_for": ["spiderman", "wonderwoman"]},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.connection
        db.get_database().users.delete_many({})
        db.get_database().teams.delete_many({})
        db.get_database().activities.delete_many({})
        db.get_database().leaderboard.delete_many({})
        db.get_database().workouts.delete_many({})

        db.get_database().users.insert_many(USERS)
        db.get_database().teams.insert_many(TEAMS)
        db.get_database().activities.insert_many(ACTIVITIES)
        db.get_database().leaderboard.insert_many(LEADERBOARD)
        db.get_database().workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db has been populated with test data.'))
