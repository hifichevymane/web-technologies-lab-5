from django.forms import ModelForm, TextInput, NumberInput, Select
from .models import Category, Product

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'product_qty', 'category']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product title'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product price'
            }),
            'product_qty': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product quantity'
            }),
            'category': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select category'
            })
        }
