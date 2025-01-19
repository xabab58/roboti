from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Wine(models.Model):
    WINE_TYPES = [
        ('red', 'Красное'),
        ('white', 'Белое'),
        ('rose', 'Розовое'),
    ]
    
    SWEETNESS_TYPES = [
        ('dry', 'Сухое'),
        ('semi_dry', 'Полусухое'),
        ('semi_sweet', 'Полусладкое'),
        ('sweet', 'Сладкое'),
    ]
    
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    wine_type = models.CharField(max_length=20, choices=WINE_TYPES)
    sweetness = models.CharField(max_length=20, choices=SWEETNESS_TYPES)
    image = models.ImageField(upload_to='wines/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0
    
    def __str__(self):
        return self.name

class WineReview(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    reviewer_name = models.CharField(max_length=100, default='Гость')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=False,
        blank=False
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.wine.name} by {self.user or 'Guest'}" 