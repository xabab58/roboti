from django.urls import path
from . import views

urlpatterns = [
    path('', views.wine_list, name='wine_list'),
    path('<int:pk>/', views.wine_detail, name='wine_detail'),
    path('add/', views.add_wine, name='add_wine'),
    path('review/add/', views.add_wine_review, name='add_wine_review'),
] 