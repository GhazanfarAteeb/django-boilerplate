from django.contrib import admin

from user import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = [
        'uid', 'created_at', 'last_login',
    ]
    search_fields = ['email', 'uid', ]
    list_display = (
        'email', 'first_name', 'last_name', 'is_email_verified', 'is_phone_verified', 'created_at',
    )
    fields = [
        'email', 'first_name', 'last_name', 'phone', 'avatar',
        'is_staff', 'is_email_verified', 'is_phone_verified', 'password',
        'is_active', 'created_at', 'last_login',
    ]

