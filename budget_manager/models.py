from django.db import models
from django.contrib.auth.models import User


class Sources(models.Model):
    source_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.source_name} by {self.user}'


class Currencies(models.Model):
    name = models.CharField(max_length=20)
    currency_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category_name} by {self.user}'


class Income(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    income_date = models.DateField()
    source = models.ForeignKey(Sources, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currencies, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.amount} from {self.source}'


class Expenses(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    expense_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currencies, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} by {self.user} | {self.category}'
