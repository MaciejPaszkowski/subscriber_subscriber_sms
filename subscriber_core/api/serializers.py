from rest_framework import serializers
from .models import Subscriber, SubscriberSMS, Client, AppUser


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"


class SubscriberSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberSMS
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = "__all__"
