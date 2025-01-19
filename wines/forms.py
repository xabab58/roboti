from django import forms
from .models import Wine, WineReview

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'country', 'wine_type', 'sweetness', 'image']
        labels = {
            'name': 'Название вина',
            'country': 'Страна производства',
            'wine_type': 'Тип вина',
            'sweetness': 'Сладость',
            'image': 'Фото вина'
        }

class WineFilterForm(forms.Form):
    country = forms.CharField(
        label='Страна',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите страну'})
    )
    wine_type = forms.ChoiceField(
        label='Тип вина',
        choices=[('', 'Все')] + Wine.WINE_TYPES,
        required=False
    )
    sweetness = forms.ChoiceField(
        label='Сладость',
        choices=[('', 'Все')] + Wine.SWEETNESS_TYPES,
        required=False
    )

class WineReviewForm(forms.ModelForm):
    reviewer_name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        required=True
    )
    wine = forms.ModelChoiceField(
        label='Вино',
        queryset=Wine.objects.all(),
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
        model = WineReview
        fields = ['reviewer_name', 'wine', 'rating', 'comment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['reviewer_name'].initial = user.username 