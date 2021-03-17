from django.urls import path

from . import views

urlpatterns = [
    path('',views.view_collection, name='collection'),
    path('product/<str:id>/', views.view_product, name='product')
]