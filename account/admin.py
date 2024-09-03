from django.contrib import admin
from .models import CustomUser, Role



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('phone_number', 'name', 'surname', 'role', 'created_at')
    search_fields = ('name', 'surname', 'phone_number')
    list_filter = ('created_at', 'role')
