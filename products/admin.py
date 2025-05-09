from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'product_qty', 'category', 'updated_at']
    list_editable = ['price', 'product_qty', 'category']
    list_filter = ['category', 'updated_at']
    search_fields = ['title', 'category__title']
