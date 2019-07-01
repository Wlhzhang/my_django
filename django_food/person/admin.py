

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from person.models import SingDinner

admin.site.register(SingDinner)