from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView

from .models import User


class SendConfirmationCode(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = None
