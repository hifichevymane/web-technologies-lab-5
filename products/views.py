from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.urls import reverse_lazy

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = '-updated_at'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


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
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'slug': self.object.slug})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete-product.html'
    success_url = reverse_lazy('product-list')
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class CategoryListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 5
    ordering = '-created_at'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category-detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'


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
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('category-detail', kwargs={'slug': self.object.slug})


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'products/delete-category.html'
    success_url = reverse_lazy('category-list')
    context_object_name = 'category'
    slug_url_kwarg = 'slug'
