from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import AdminOnly, DoWhatYouWant
from .serializers import (
    ProfileSerializer, SendConfirmationCodeSerializer, SendTokenSerializer,
)

User = get_user_model()


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
            self.request.user.is_superuser or
            self.request.user.role == 'admin'
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
