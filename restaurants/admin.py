from django.contrib import admin
from .models import Restaurant, RestaurantReview

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'average_rating')
    search_fields = ('name',)
    list_filter = ('created_at',)
    fields = ('name', 'address', 'image')

@admin.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'reviewer_name', 'dish', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'restaurant')
    search_fields = ('restaurant__name', 'reviewer_name', 'dish', 'comment')
    fields = ('restaurant', 'reviewer_name', 'dish', 'rating', 'comment') 