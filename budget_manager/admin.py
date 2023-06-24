from django.contrib import admin
from budget_manager import models

# Register your models here.
admin.site.register(models.Source)
admin.site.register(models.Currency)
admin.site.register(models.Category)
admin.site.register(models.Income)
admin.site.register(models.Expense)
