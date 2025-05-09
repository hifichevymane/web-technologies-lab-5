from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at']
    search_fields = ['title', 'slug']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'product_qty', 'category', 'updated_at']
    list_editable = ['slug', 'price', 'product_qty']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'updated_at']
    search_fields = ['title', 'slug', 'category__title']
