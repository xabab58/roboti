from django import forms
from .models import Restaurant, RestaurantReview

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'image']
        labels = {
            'name': 'Имя ресторана',
            'image': 'Фото ресторана'
        }
        error_messages = {
            'name': {
                'required': 'Это поле обязательно для заполнения'
            },
            'image': {
                'required': 'Необходимо добавить фото ресторана'
            }
        }

class ReviewForm(forms.ModelForm):
    reviewer_name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        required=True
    )
    restaurant = forms.ModelChoiceField(
        label='Ресторан',
        queryset=Restaurant.objects.all(),
        required=True
    )
    dish = forms.CharField(
        label='Название блюда',
        initial='Все подряд',
        required=True
    )
    rating = forms.IntegerField(
        label='Оценка',
        min_value=1,
        max_value=10,
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'От 1 до 10'})
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = RestaurantReview
        fields = ['reviewer_name', 'restaurant', 'dish', 'rating', 'comment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['reviewer_name'].initial = user.username 