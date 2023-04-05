from django.test import TestCase

# from api.models import Subscriber
from api.models import Subscriber, SubscriberSMS, Client, AppUser


class TestModels(TestCase):
    def setUp(self):
        self.subscriber = Subscriber.objects.create(
            id=1, create_date="2023-04-01", email="test1@test.com", gdpr_consent=True
        )
        self.subscriber_sms = SubscriberSMS.objects.create(
            id=1, create_date="2023-04-01", phone="1234567890", gdpr_consent=True
        )
        self.client = Client.objects.create(
            id=1, create_date="2023-04-01", phone="1234567890", email="test1@test.com"
        )
        self.user = AppUser.objects.create(
            id=1,
            create_date="2023-04-01",
            phone="1234567890",
            email="test1@test.com",
            gdpr_consent=True,
        )

    def test_subscriber_model(self):
        self.assertEqual(self.subscriber.email, "test1@test.com")
        self.assertTrue(self.subscriber.gdpr_consent)

    def test_subscriber_sms_model(self):
        self.assertEqual(self.subscriber_sms.phone, "1234567890")
        self.assertTrue(self.subscriber.gdpr_consent)

    def test_client_model(self):
        self.assertEqual(self.client.phone, "1234567890")
        self.assertEqual(self.client.email, "test1@test.com")

    def test_user_model(self):
        self.assertEqual(self.user.phone, "1234567890")
        self.assertEqual(self.user.email, "test1@test.com")
        self.assertTrue(self.user.gdpr_consent)
