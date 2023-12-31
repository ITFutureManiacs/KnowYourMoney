import datetime

from django.core.validators import MinValueValidator
from django.db import models

from KnowYourMoney import settings


class Source(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Currency(models.Model):
    name = models.CharField(max_length=20)
    currency_code = models.CharField(max_length=10)

    def __str__(self):
        return self.currency_code


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.name}"


class Income(models.Model):
    amount = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0.01, "Wartość musi być większa od 0")],
    )
    income_date = models.DateField(default=datetime.date.today)
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.amount} from {self.source}"


class Expense(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0.01, "Wartość musi być większa od 0")],
    )
    expense_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.ForeignKey(
        Currency, on_delete=models.DO_NOTHING, default=Currency.currency_code == "PLN"
    )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} by {self.user} | {self.category}"
