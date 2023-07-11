from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import MyUnicodeUsernameValidator


class CustomUser(AbstractUser):
    username_validator = MyUnicodeUsernameValidator()

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Uzupełnij. 150 znaków lub mniej. Litery, cyfry i znaki: @/./+/-/_.",
        validators=[username_validator],
        error_messages={"unique": "Podany login jest już zajęty."},
    )

    email = models.EmailField(
        unique=True, error_messages={"unique": "Podany adres email już istnieje"}
    )
