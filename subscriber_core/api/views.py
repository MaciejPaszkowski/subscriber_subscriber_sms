from rest_framework import generics
from .models import Subscriber, SubscriberSMS, Client, AppUser
from .serializers import (
    SubscriberSerializer,
    SubscriberSMSSerializer,
    ClientSerializer,
    AppUserSerializer,
)


class SubscriberList(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class SubscriberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class SubscriberSMSList(generics.ListCreateAPIView):
    queryset = SubscriberSMS.objects.all()
    serializer_class = SubscriberSMSSerializer


class SubscriberSMSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriberSMS.objects.all()
    serializer_class = SubscriberSMSSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
