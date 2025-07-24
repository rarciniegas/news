from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ( "email", "username", "age", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),  # Add custom fields here
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age",)}),  # Add custom fields here
    )
# Register the custom user model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
