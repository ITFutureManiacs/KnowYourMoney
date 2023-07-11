from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models

admin.site.register(models.CustomUser, UserAdmin)
