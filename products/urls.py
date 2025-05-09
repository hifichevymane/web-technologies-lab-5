from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('', ProductListView.as_view(), name='product-list'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
