from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status
from rest_framework.generics import (
    CreateAPIView, RetrieveUpdateAPIView, get_object_or_404,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Comment, Review, Title
from .permissions import AdminOnly, DoWhatYouWant, IsAuthAdmModerOrReadOnly
from .serializers import (
    CommentSerializer, ProfileSerializer, ReviewSerializer,
    SendConfirmationCodeSerializer, SendTokenSerializer,
)

User = get_user_model()


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthAdmModerOrReadOnly)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        queryset = title.reviews.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthAdmModerOrReadOnly)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        review = get_object_or_404(
            Review, title=self.kwargs.get('title_id'),
            id=self.kwargs.get('review_id')
        )
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SendConfirmationCodeView(CreateAPIView):
    serializer_class = SendConfirmationCodeSerializer
    permission_classes = [
        DoWhatYouWant,
    ]

    def perform_create(self, serializer):
        confirmation_code = uuid4()
        email = serializer.validated_data['email']
        send_mail(
            subject='Confirm your registration on yamdb.',
            message=(
                'Для подтверждения регистрации отправьте запросом этот код:\n'
                f'{confirmation_code}'
            ),
            from_email='myname@mydomain.ru',
            recipient_list=[
                email,
            ],
            fail_silently=False,
        )
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.confirmation_code = confirmation_code
            user.save()
        else:
            serializer.save(
                confirmation_code=str(confirmation_code),
                is_active=False,
            )


class SendTokenView(CreateAPIView):
    serializer_class = SendTokenSerializer
    permission_classes = [
        DoWhatYouWant,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = get_object_or_404(
                User,
                email=serializer.validated_data['email'],
            )
            user.is_active = True
            user.save()
            return Response(
                {
                    'token': serializer.validated_data['token'],
                },
                status=status.HTTP_200_OK,
            )


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return User.objects.get(
            pk=self.request.user.pk
        )

    def perform_update(self, serializer):
        if not (
            self.request.user.is_superuser
            or self.request.user.role == 'admin'
        ):
            serializer.validated_data['role'] = 'user'
        serializer.save()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        AdminOnly,
    ]
    lookup_field = 'username'
