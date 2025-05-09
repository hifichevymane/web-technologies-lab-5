from django.views.generic import ListView, CreateView, DetailView
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.urls import reverse_lazy

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = 'id'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/new-product.html'
    success_url = reverse_lazy('product-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 4

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/new-category.html'
    success_url = reverse_lazy('category-list')
