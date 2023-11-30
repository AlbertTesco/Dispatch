import random
import string

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Почта')
    verified = models.BooleanField(default=False, verbose_name='Активация')
    verification_code = models.CharField(unique=True, max_length=10, verbose_name='Код верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def generate_verification_code(self, length=10):
        """Generation code for verification"""

        letters_and_digits = string.ascii_letters + string.digits
        code = ''.join(random.choice(letters_and_digits) for i in range(length))
        self.verification_code = code
        self.save()

    def activate_user(self):
        """Activates the user"""

        self.verified = True
        self.save()

    def deactivate_user(self):
        """Deactivates the user"""

        self.verified = False
        self.save()

    def is_verified(self):
        """Get whether the user is verified"""
        return self.verified

    def send_verification_code(self):
        """Sending verification code to user"""
        print(self.email)
        send_mail(
            subject='Код верификации',
            message=f'Ваш код верификации: {self.verification_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.email]
        )
