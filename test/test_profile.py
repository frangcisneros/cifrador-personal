import unittest
from app import create_app, db
from app.models import Profile
from app.services import ProfileService
import os

profile_service = ProfileService()


class ProfileTestCase(unittest.TestCase):

    def setUp(self):
        os.environ["FLASK_CONTEXT"] = "testing"
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.NAME = "Client"
        self.profile = Profile(name=self.NAME)
        profile_service.save(self.profile)

    def tearDown(self):
        profile_service.delete(self.profile)
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_profile_save(self):
        self.assertGreaterEqual(self.profile.id, 1)
        self.assertEqual(self.profile.name, self.NAME)

    def test_profile_delete(self):
        profile_service.delete(self.profile)
        self.assertIsNone(profile_service.find(self.profile))

    def test_profile_update(self):
        self.profile.name = "Client Updated"
        profile_service.update(self.profile, self.profile.id)
        self.assertEqual(self.profile.name, "Client Updated")

    def test_profile_find(self):
        profile = profile_service.find(self.profile.id)
        self.assertIsNotNone(profile)

    def test_all(self):
        profiles = profile_service.all()
        self.assertGreaterEqual(len(profiles), 1)
