from django.views.generic import ListView
from .models import Product, Category

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = 'id'

class CategoryListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 4
