from django.urls import path
from .views import ProductListView, CategoryListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
