from django.contrib import admin
from .models import User, UserProfile

class UserProfileInline(admin.TabularInline):
    model = UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]

admin.site.register(User, UserProfileAdmin)