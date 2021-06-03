from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    'users',
    views.UserViewSet,
    basename='users'
)

urlpatterns = [
    path(
        'v1/auth/email/',
        views.SendConfirmationCodeView.as_view(),
    ),
    path(
        'v1/auth/token/',
        views.SendTokenView.as_view(),
    ),
    path(
        'v1/users/me/',
        views.ProfileView.as_view(),
    ),
    path(
        'v1/',
        include(router.urls)
    ),
]
