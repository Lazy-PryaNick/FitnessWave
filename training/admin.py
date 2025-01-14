from django.contrib import admin
from .models import (
	ContactProfile,
	UserProfile,
	Product,
)
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price')
