from django.test import TestCase
from api.models import AppUser, Client, Subscriber, SubscriberSMS
from api.serializers import (
    AppUserSerializer,
    ClientSerializer,
    SubscriberSerializer,
    SubscriberSMSSerializer,
)

import datetime
import zoneinfo


class TestSerializers(TestCase):
    def setUp(self):
        self.subscriber_data = {
            "id": 1,
            "create_date": datetime.datetime(
                2022, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")
            ),
            "email": "subscriber@example.com",
            "gdpr_consent": True,
        }
        self.subscriber_sms_data = {
            "id": 2,
            "create_date": datetime.datetime(
                2022, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")
            ),
            "phone": "+1234567890",
            "gdpr_consent": False,
        }
        self.client_data = {
            "id": 3,
            "create_date": datetime.datetime(
                2022, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")
            ),
            "email": "client@example.com",
            "phone": "+1234567890",
        }
        self.user_data = {
            "id": 4,
            "create_date": datetime.datetime(
                2022, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key="UTC")
            ),
            "email": "user@example.com",
            "phone": "+1234567890",
            "gdpr_consent": True,
        }

    def test_subscriber_serializer(self):
        serializer = SubscriberSerializer(data=self.subscriber_data)
        self.assertTrue(serializer.is_valid())

        subscriber = serializer.save()
        self.assertEqual(subscriber.id, self.subscriber_data["id"])
        self.assertEqual(subscriber.create_date, self.subscriber_data["create_date"])
        self.assertEqual(subscriber.email, self.subscriber_data["email"])
        self.assertEqual(subscriber.gdpr_consent, self.subscriber_data["gdpr_consent"])

    def test_subscriber_sms_serializer(self):
        serializer = SubscriberSMSSerializer(data=self.subscriber_sms_data)
        self.assertTrue(serializer.is_valid())

        subscriber_sms = serializer.save()
        self.assertEqual(subscriber_sms.id, self.subscriber_sms_data["id"])
        self.assertEqual(
            subscriber_sms.create_date, self.subscriber_sms_data["create_date"]
        )
        self.assertEqual(subscriber_sms.phone, self.subscriber_sms_data["phone"])
        self.assertEqual(
            subscriber_sms.gdpr_consent, self.subscriber_sms_data["gdpr_consent"]
        )

    def test_client_serializer(self):
        serializer = ClientSerializer(data=self.client_data)
        self.assertTrue(serializer.is_valid())

        client = serializer.save()
        self.assertEqual(client.id, self.client_data["id"])
        self.assertEqual(client.create_date, self.client_data["create_date"])
        self.assertEqual(client.email, self.client_data["email"])
        self.assertEqual(client.phone, self.client_data["phone"])

    def test_user_serializer(self):
        serializer = AppUserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        self.assertEqual(user.id, self.user_data["id"])
        self.assertEqual(user.create_date, self.user_data["create_date"])
        self.assertEqual(user.email, self.user_data["email"])
        self.assertEqual(user.phone, self.user_data["phone"])
        self.assertEqual(user.gdpr_consent, self.user_data["gdpr_consent"])
