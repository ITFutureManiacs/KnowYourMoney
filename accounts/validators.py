from django.utils.translation import ngettext
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, CommonPasswordValidator, \
    NumericPasswordValidator,MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MyUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def get_help_text(self):
        return (
            "Twoje hasło nie może być zbyt podobne do informacji osobistych(np. loginu)")


class MyCommonPasswordValidator(CommonPasswordValidator):
    def get_help_text(self):
        return ("Twoje hasło nie może być powszechnie używanym hasłem.")

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("To hasło jest zbyt powszechne."),
                code="password_too_common",
            )


class MyNumericPasswordValidator(NumericPasswordValidator):
    def get_help_text(self):
        return ("Twoje hasło nie może składać się tylko z cyfr.")

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("To hasło składa się tylko z cyfr."),
                code="password_entirely_numeric",
            )


class MyMinimumLengthValidator(MinimumLengthValidator):
    def get_help_text(self):
        return ngettext(
            "Twoje hasło powinno zawierać %(min_length)d znaków.",
            "Twoje hasło powinno zawierać %(min_length)d znaków.",
            self.min_length,
        ) % {"min_length": self.min_length}

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "To hasło jest za krótkie. Powinno zawierać przynajmniej "
                    "%(min_length)d znaków.",
                    "To hasło jest za krótkie. Powinno zawierać przynajmniej "
                    "%(min_length)d znaków.",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )
