from django.urls import path
from . import views

urlpatterns = [
    path("subscribers", views.SubscriberList.as_view()),
    path("subscribers/<int:pk>", views.SubscriberDetail.as_view()),
    path("subscribers-sms", views.SubscriberSMSList.as_view()),
    path("subscribers-sms/<int:pk>", views.SubscriberSMSDetail.as_view()),
    path("clients", views.ClientList.as_view()),
    path("clients/<int:pk>", views.ClientDetail.as_view()),
    path("users", views.AppUserList.as_view()),
    path("users/<int:pk>", views.AppUserDetail.as_view()),
]
