from django.contrib import admin

# Register your models here.
from .models import UserProfile, Group, Task

admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Group)