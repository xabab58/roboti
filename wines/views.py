from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Wine, WineReview
from .forms import WineForm, WineReviewForm, WineFilterForm
import random

def wine_list(request):
    wines = Wine.objects.all()
    filter_form = WineFilterForm(request.GET)
    
    if filter_form.is_valid():
        if filter_form.cleaned_data['country']:
            wines = wines.filter(country__icontains=filter_form.cleaned_data['country'])
        if filter_form.cleaned_data['wine_type']:
            wines = wines.filter(wine_type=filter_form.cleaned_data['wine_type'])
        if filter_form.cleaned_data['sweetness']:
            wines = wines.filter(sweetness=filter_form.cleaned_data['sweetness'])
    
    return render(request, 'wines/list.html', {
        'wines': wines,
        'filter_form': filter_form
    })

def wine_detail(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    reviews = wine.reviews.all().order_by('-created_at')
    return render(request, 'wines/detail.html', {
        'wine': wine,
        'reviews': reviews,
    })

@login_required
def add_wine(request):
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wine_list')
    else:
        form = WineForm()
    return render(request, 'wines/add.html', {'form': form})

def add_wine_review(request):
    if request.method == 'POST':
        form = WineReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user if request.user.is_authenticated else None
            review.save()
            return redirect('wine_detail', pk=form.cleaned_data['wine'].pk)
    else:
        initial_wine = request.GET.get('wine')
        form = WineReviewForm(
            user=request.user,
            initial={'wine': initial_wine} if initial_wine else None
        )
    return render(request, 'wines/add_review.html', {'form': form}) 