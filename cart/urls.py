from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', views.update_cart, name='update_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('toggle_discount/', views.toggle_discount, name='toggle_discount'),
    path('repeat/<order_number>/', views.replicate_cart, name='replicate_cart'),
]
