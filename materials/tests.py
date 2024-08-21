from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User
from rest_framework import status
from django.urls import reverse


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test3@test.ru")
        self.course = Course.objects.create(name="test_course", description="test")
        self.lesson = Lesson.objects.create(
            name="test_lesson", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "test_lesson")

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "name": "test_lesson_create",
            "course": self.course.pk,
            "owner": self.user.pk,
            "description": "test_lesson_create",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name": "test_lesson_update"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.pk).name, "test_lesson_update"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test5@test.ru")
        self.course = Course.objects.create(
            name="test_course", description="test_course"
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("materials:subscription_list")

    def test_subscription_create(self):
        data = {"owner": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscription_delete(self):
        Subscription.objects.create(owner=self.user, course=self.course)
        data = {
            "owner": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)
