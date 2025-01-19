from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('add/', views.add_restaurant, name='add_restaurant'),
    path('review/add/', views.add_review, name='add_review'),
] 