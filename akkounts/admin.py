from django.contrib import admin
from .models import User,Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('username',)

