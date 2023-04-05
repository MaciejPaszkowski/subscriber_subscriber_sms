from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.models import Subscriber, SubscriberSMS, AppUser
from api.models import Client as MyClient


class SubscriberAPITest(APITestCase):
    def setUp(self):
        self.client_post = APIRequestFactory()
        self.subscriber1 = Subscriber.objects.create(
            id=1,
            create_date="2022-01-01",
            email="subscriber1@example.com",
            gdpr_consent=True,
        )
        self.subscriber2 = Subscriber.objects.create(
            id=2,
            create_date="2022-01-02",
            email="subscriber2@example.com",
            gdpr_consent=False,
        )
        self.subscriber_sms = SubscriberSMS.objects.create(
            id=1, create_date="2022-01-03", phone="123456789", gdpr_consent=True
        )
        self.my_client = MyClient.objects.create(
            id=1,
            create_date="2022-01-04",
            email="client@example.com",
            phone="987654321",
        )
        self.user = AppUser.objects.create(
            id=1,
            create_date="2022-01-05",
            email="user@example.com",
            phone="123123123",
            gdpr_consent=False,
        )

    def test_list_subscribers(self):
        url = reverse("subscriber-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_subscriber(self):
        url = reverse("subscriber-list")
        data = {
            "id": 3,
            "create_date": "2022-01-06",
            "email": "subscriber3@example.com",
            "gdpr_consent": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscriber.objects.count(), 3)

    def test_retrieve_subscriber(self):
        url = reverse("subscriber-detail", args=[self.subscriber1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "subscriber1@example.com")

    def test_update_subscriber(self):
        url = reverse("subscriber-detail", args=[self.subscriber1.id])
        data = {"email": "new-email@example.com", "gdpr_consent": False}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.subscriber1.refresh_from_db()
        self.assertEqual(self.subscriber1.email, "new-email@example.com")
        self.assertFalse(self.subscriber1.gdpr_consent)

    def test_delete_subscriber(self):
        url = reverse("subscriber-detail", args=[self.subscriber1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscriber.objects.count(), 1)
