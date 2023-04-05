from django.db import models


class Subscriber(models.Model):
    id = models.IntegerField(primary_key=True)
    create_data = models.DateTimeField()
    email = models.CharField(max_length=240, unique=True)
    gdpr_consent = models.BooleanField()


class SubscriberSMS(models.Model):
    id = models.IntegerField(primary_key=True)
    create_data = models.DateTimeField()
    phone = models.CharField(max_length=20, unique=True)
    gdpr_consent = models.BooleanField()


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    create_data = models.DateTimeField()
    email = models.CharField(max_length=240, unique=True)
    phone = models.CharField(max_length=20)


class AppUser(models.Model):
    id = models.IntegerField(primary_key=True)
    create_data = models.DateTimeField()
    email = models.CharField(max_length=240)
    phone = models.CharField(max_length=20)
    gdpr_consent = models.BooleanField()
