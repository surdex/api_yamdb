from django.urls import path

from . import views

urlpatterns = [
    path(
        'v1/auth/email/',
        views.SendConfirmationCodeView.as_view()
    ),
    path(
        'v1/auth/token/',
        views.SendTokenView.as_view(),
        name='token_obtain_pair'
    ),
]
