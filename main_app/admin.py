from django.contrib import admin
from django.utils.html import format_html
from .models import UserInfo, Product

# --- UserInfo Admin ---
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "city", "hobby", "favorite_food")
    search_fields = ("user__username", "city", "hobby", "favorite_food")

# --- Product Admin ---
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "photo_tag")
    list_filter = ("is_available",)
    search_fields = ("name", "description")

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />',
                obj.photo.url
            )
        return "No Image"

    photo_tag.short_description = "Photo"
