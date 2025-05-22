from django.urls import path, include
from tastypie.api import Api
from .models import CategoryResource, ProductResource

category_resource = Api(api_name='v1')
category_resource.register(CategoryResource())

product_resource = Api(api_name='v1')
product_resource.register(ProductResource())

urlpatterns = [
    path('', include(category_resource.urls)),
    path('', include(product_resource.urls))
]
