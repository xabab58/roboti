from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Restaurant, RestaurantReview
from .forms import RestaurantForm, ReviewForm
import random

def restaurant_list(request):
    restaurants = list(Restaurant.objects.all())
    if len(restaurants) > 10:
        restaurants = random.sample(restaurants, 10)
    return render(request, 'restaurants/list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reviews = restaurant.reviews.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user if request.user.is_authenticated else None
            review.save()
            return redirect('restaurant_detail', pk=pk)
    else:
        form = ReviewForm(
            user=request.user,
            initial={'restaurant': restaurant}
        )
        
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'form': form
    })

@login_required
def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/add.html', {'form': form})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user if request.user.is_authenticated else None
            review.save()
            return redirect('restaurant_detail', pk=form.cleaned_data['restaurant'].pk)
    else:
        form = ReviewForm(user=request.user)
    
    return render(request, 'restaurants/add_review.html', {'form': form}) 