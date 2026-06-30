from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserProfile



# Remove Groups from admin panel
admin.site.unregister(Group)