from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class UserModelTest(TestCase):

    def test_user_creation_fields(self):
        user = User.objects.create_user(
            username="navruz",
            password="password123",
            bio="Full-stack dasturchi",
            age=22
        )
        self.assertEqual(user.username, "navruz")
        self.assertEqual(user.bio, "Full-stack dasturchi")
        self.assertEqual(user.age, 22)


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="navruz", password="password123")

    def test_profile_creation_fields(self):
        profile = Profile.objects.create(
            user=self.user,
            bio="Men haqimda qisqacha ma'lumot..."
        )
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.bio, "Men haqimda qisqacha ma'lumot...")

    def test_profile_str_method(self):
        profile = Profile.objects.create(user=self.user, bio="...")
        self.assertEqual(str(profile), "navruz profili")