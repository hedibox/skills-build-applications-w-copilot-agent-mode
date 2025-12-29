from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com')
        team = Team.objects.create(name='TeamTest')
        team.members.add(user)
        self.assertEqual(team.name, 'TeamTest')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser', email='activity@example.com')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, calories_burned=200, date='2025-01-01')
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio session', difficulty='Medium')
        self.assertEqual(workout.name, 'Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='LBTeam')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(leaderboard.total_points, 100)
