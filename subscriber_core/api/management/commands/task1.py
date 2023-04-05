import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction
from api.models import Subscriber, SubscriberSMS, Client, AppUser


class Command(BaseCommand):
    help = "Migrates records from Subscriber and SubscriberSMS models to User model"

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        subscriber_conflicts = []
        subscriber_sms_conflicts = []
        client_phone_conflicts = []
        client_email_conflicts = []
        now = datetime.now()
        with transaction.atomic():
            for subscriber in Subscriber.objects.all():
                if AppUser.objects.filter(email=subscriber.email).exists():
                    continue

                client = Client.objects.filter(email=subscriber.email).first()
                if client:
                    user = AppUser.objects.filter(phone=client.phone).first()
                    if user:
                        if user.email != client.email:
                            subscriber_conflicts.append(
                                (subscriber.id, subscriber.email)
                            )
                    else:
                        if (
                            Client.objects.exclude(id=client.id)
                            .filter(phone=client.phone)
                            .exists()
                        ):
                            client_phone_conflicts.append(client.phone)
                        else:
                            user = AppUser.objects.create(
                                create_date=subscriber.create_date,
                                email=client.email,
                                phone=client.phone,
                                gdpr_consent=subscriber.gdpr_consent,
                            )
                            user.save()
                else:
                    user = AppUser.objects.create(
                        create_date=subscriber.create_date,
                        email=subscriber.email,
                        phone="",
                        gdpr_consent=subscriber.gdpr_consent,
                    )
                    user.save()

            for subscriber_sms in SubscriberSMS.objects.all():
                if AppUser.objects.filter(phone=subscriber_sms.phone).exists():
                    continue

                client = Client.objects.filter(phone=subscriber_sms.phone).first()
                if client:
                    user = AppUser.objects.filter(email=client.email).first()
                    if user:
                        if user.phone != client.phone:
                            subscriber_sms_conflicts.append(
                                subscriber_sms.id, subscriber_sms.phone
                            )

                    else:
                        if (
                            Client.objects.exclude(id=client.id)
                            .filter(email=client.email)
                            .exists()
                        ):
                            client_email_conflicts.append(client.email)
                        else:
                            user = AppUser.objects.create(
                                create_date=subscriber_sms.create_date,
                                email=client.email,
                                phone=client.phone,
                                gdpr_consent=subscriber_sms.gdpr_consent,
                            )
                            user.save()
                else:
                    user = AppUser.objects.create(
                        create_date=subscriber_sms.create_date,
                        email="",
                        phone=subscriber_sms.phone,
                        gdpr_consent=subscriber_sms.gdpr_consent,
                    )
                    user.save()

        with open("subscriber_conflicts.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(subscriber_conflicts)

        with open("subscriber_sms_conflicts.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(subscriber_sms_conflicts)

        with open("client_phone_conflicts.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(client_phone_conflicts)

        with open("client_email_conflicts.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(client_email_conflicts)

        self.stdout.write(
            self.style.SUCCESS(
                "Migrates records from Subscriber and SubscriberSMS models to User model DONE"
            )
        )
