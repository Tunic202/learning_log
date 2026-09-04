from django.contrib.auth.models import User
from django.test import TestCase

from .models import Entry, Topic


class TopicModelTest(TestCase):
    """Tests for the Topic model."""

    def test_topic_string_representation(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        topic = Topic.objects.create(
            text="Python Programming",
            owner=user,
        )

        self.assertEqual(str(topic), "Python Programming")


class EntryModelTest(TestCase):
    """Tests for the Entry model."""

    def test_entry_string_representation(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        topic = Topic.objects.create(
            text="Python Programming",
            owner=user,
        )
        entry = Entry.objects.create(
            topic=topic,
            text="I learned how to use Django models.",
        )

        self.assertEqual(
            str(entry),
            "I learned how to use Django models.",
        )


class TopicViewTest(TestCase):
    """Tests for topic views and ownership."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123",
        )

        self.topic = Topic.objects.create(
            text="Python Programming",
            owner=self.user,
        )

        self.other_topic = Topic.objects.create(
            text="Django Development",
            owner=self.other_user,
        )

    def test_topics_requires_login(self):
        response = self.client.get("/topics/")

        self.assertEqual(response.status_code, 302)

    def test_user_can_view_own_topic(self):
        self.client.force_login(self.user)

        response = self.client.get(
            f"/topics/{self.topic.id}/"
        )

        self.assertEqual(response.status_code, 200)

    def test_user_cannot_view_another_users_topic(self):
        self.client.force_login(self.user)

        response = self.client.get(
            f"/topics/{self.other_topic.id}/"
        )

        self.assertEqual(response.status_code, 404)

    def test_user_can_create_topic(self):
        self.client.force_login(self.user)

        response = self.client.post(
            "/new_topic/",
            {"text": "Django Testing"},
        )

        self.assertRedirects(response, "/topics/")

        topic = Topic.objects.get(text="Django Testing")

        self.assertEqual(topic.owner, self.user)


class EntryViewTest(TestCase):
    """Tests for entry views and ownership."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123",
        )

        self.topic = Topic.objects.create(
            text="Python Programming",
            owner=self.user,
        )

        self.other_topic = Topic.objects.create(
            text="Django Development",
            owner=self.other_user,
        )

        self.entry = Entry.objects.create(
            topic=self.topic,
            text="I learned about Django views.",
        )

        self.other_entry = Entry.objects.create(
            topic=self.other_topic,
            text="Private learning notes.",
        )

    def test_user_cannot_add_entry_to_another_users_topic(self):
        self.client.force_login(self.user)

        response = self.client.get(
            f"/new_entry/{self.other_topic.id}/"
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_edit_another_users_entry(self):
        self.client.force_login(self.user)

        response = self.client.get(
            f"/edit_entry/{self.other_entry.id}/"
        )

        self.assertEqual(response.status_code, 404)

    def test_user_can_create_entry(self):
        self.client.force_login(self.user)

        response = self.client.post(
            f"/new_entry/{self.topic.id}/",
            {"text": "I learned how Django forms work."},
        )

        self.assertRedirects(
            response,
            f"/topics/{self.topic.id}/",
        )

        entry = Entry.objects.get(
            text="I learned how Django forms work."
        )

        self.assertEqual(entry.topic, self.topic)

    def test_user_can_edit_entry(self):
        self.client.force_login(self.user)

        response = self.client.post(
            f"/edit_entry/{self.entry.id}/",
            {"text": "I updated my Django learning notes."},
        )

        self.assertRedirects(
            response,
            f"/topics/{self.topic.id}/",
        )

        self.entry.refresh_from_db()

        self.assertEqual(
            self.entry.text,
            "I updated my Django learning notes.",
        )
