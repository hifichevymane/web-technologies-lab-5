from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
]
