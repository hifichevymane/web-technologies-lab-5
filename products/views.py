from django.views.generic import ListView, CreateView, DetailView, UpdateView
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/new-product.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update-product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.pk})


class CategoryListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 4


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category-detail.html'
    context_object_name = 'category'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/new-category.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/update-category.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse_lazy('category-detail', kwargs={'pk': self.object.pk})
