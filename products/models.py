from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)  # Making it nullable initially
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['created_at']

class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)  # Making it nullable initially
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['updated_at']
