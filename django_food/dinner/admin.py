from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from dinner.models import DinnerInfo

admin.site.register(DinnerInfo)