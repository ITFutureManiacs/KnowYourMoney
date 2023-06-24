from django.contrib import admin
from budget_manager import models

# Register your models here.
admin.site.register(models.Sources)
admin.site.register(models.Currencies)
admin.site.register(models.Categories)
admin.site.register(models.Income)
admin.site.register(models.Expenses)
