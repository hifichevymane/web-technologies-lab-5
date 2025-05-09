from django.urls import path
from .views import ProductListView, CategoryListView, ProductCreateView, CategoryCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
]
