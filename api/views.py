from uuid import uuid4
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import DoWhatYouWant
from .serializers import SendConfirmationCodeSerializer, SendTokenSerializer


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
