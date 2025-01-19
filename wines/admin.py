from django.contrib import admin
from .models import Wine, WineReview

@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'wine_type', 'sweetness', 'created_at', 'average_rating')
    list_filter = ('wine_type', 'sweetness', 'country', 'created_at')
    search_fields = ('name', 'country')
    fields = ('name', 'country', 'wine_type', 'sweetness', 'image')

@admin.register(WineReview)
class WineReviewAdmin(admin.ModelAdmin):
    list_display = ('wine', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'wine')
    search_fields = ('wine__name', 'reviewer_name', 'comment')
    fields = ('wine', 'reviewer_name', 'rating', 'comment') 