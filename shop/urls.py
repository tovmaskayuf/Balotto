from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop_home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail')
]