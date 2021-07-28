from django import forms
from .models import Review, Eating, HashTag

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['score', 'image', 'body', 'pub_date', 'salty_taste', 'sweet_taste', 'spicy_taste']