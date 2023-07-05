from django.utils.translation import ngettext
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, CommonPasswordValidator, \
    NumericPasswordValidator,MinimumLengthValidator


class MyUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def get_help_text(self):
        return (
            "Twoje hasło nie może być zbyt podobne do informacji osobistych(np. loginu)")


class MyCommonPasswordValidator(CommonPasswordValidator):
    def get_help_text(self):
        return ("Twoje hasło nie może być powszechnie używanym hasłem.")


class MyNumericPasswordValidator(NumericPasswordValidator):
    def get_help_text(self):
        return ("Twoje hasło nie może składać się tylko z cyfr.")


class MyMinimumLengthValidator(MinimumLengthValidator):
    def get_help_text(self):
        return ngettext(
            "Twoje hasło powinno zawierać %(min_length)d znaków.",
            "Twoje hasło powinno zawierać %(min_length)d znaków.",
            self.min_length,
        ) % {"min_length": self.min_length}
