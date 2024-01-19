from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Room, Topic, Message

# Register your models here.
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)