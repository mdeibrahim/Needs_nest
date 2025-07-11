# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'full_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups & Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'full_name')
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
