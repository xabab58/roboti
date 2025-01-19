from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    image = models.ImageField(upload_to='restaurants/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0
    
    def __str__(self):
        return self.name

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    reviewer_name = models.CharField(max_length=100, default='Гость')
    dish = models.CharField(max_length=200, default='Все подряд')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=False,
        blank=False
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.restaurant.name} by {self.reviewer_name}" 