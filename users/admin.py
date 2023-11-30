from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'verified', 'verification_code', 'is_active', 'is_staff')
