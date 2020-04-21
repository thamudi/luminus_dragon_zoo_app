from django import forms

from .models import Dragon, Location


class DragonForm(forms.ModelForm):
    class Meta:
        model = Dragon
        fields = [
            'name',
            'age',
            'fav_food',
            'location'
        ]
