from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    ProfileView,
    ReviewViewSet,
    SendConfirmationCodeView,
    SendTokenView,
    UserViewSet,
)


v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='Review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)
v1_router.register(
    'users',
    UserViewSet,
    basename='users'
)

api_v1_urlpatterns = [
    path(
        'auth/email/',
        SendConfirmationCodeView.as_view(),
    ),
    path(
        'auth/token/',
        SendTokenView.as_view(),
    ),
    path(
        'users/me/',
        ProfileView.as_view(),
    ),
    path('', include(v1_router.urls))
]

urlpatterns = [
    path('v1/', include(api_v1_urlpatterns))
]
