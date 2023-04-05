from django.core.management.base import BaseCommand
from api.models import Subscriber, SubscriberSMS, AppUser


class Command(BaseCommand):
    help = "Migrates gdpr_consent from Subscriber and SubscriberSMS to User"

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.exclude(
            email__in=AppUser.objects.values_list("email", flat=True)
        )
        for subscriber in subscribers:
            corresponding_user = AppUser.objects.filter(phone=subscriber.phone).first()
            if (
                corresponding_user
                and corresponding_user.create_date < subscriber.create_date
            ):
                corresponding_user.gdpr_consent = subscriber.gdpr_consent
                corresponding_user.save()

        subscriberssms = SubscriberSMS.objects.exclude(
            phone__in=AppUser.objects.values_list("phone", flat=True)
        )
        for subscribersms in subscriberssms:
            corresponding_user = AppUser.objects.filter(
                email=subscribersms.email
            ).first()
            if (
                corresponding_user
                and corresponding_user.create_date < subscribersms.create_date
            ):
                corresponding_user.gdpr_consent = subscribersms.gdpr_consent
                corresponding_user.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully migrated gdpr_consent from Subscriber and SubscriberSMS to User."
            )
        )
