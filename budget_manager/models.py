from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sources(models.Model):
    source_name = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50, null=True)


class Currencies(models.Model):
    name = models.CharField(max_length=20)
    currency_code = models.CharField(max_length=10)


class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50, null=True)


class Income(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    source_id = models.ForeignKey(Sources, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    currency_id = models.ForeignKey(Currencies, on_delete=models.DO_NOTHING)


class Expenses(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    currency_id = models.ForeignKey(Currencies, on_delete=models.DO_NOTHING)
    Category_id = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
