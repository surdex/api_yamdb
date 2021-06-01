from django.urls import path

from . import views

urlpatterns = [
    path('v1/auth/email', views.SendConfirmationCode.as_view())
]
