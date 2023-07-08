from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.backends import BaseBackend

User = get_user_model()


class EmailOrLoginUsernameAuthenticationBackend(BaseBackend):
    @staticmethod
    def authenticate(request, username=None, password=None):
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username)
            )

        except User.DoesNotExist:
            return None

        if user and check_password(password, user.password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
