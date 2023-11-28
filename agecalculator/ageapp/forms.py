from django import forms
from .models import Person

class AgeForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['birthdate']
        widgets = {
            'birthdate': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
        help_texts = {
            'birthdate': 'Please enter your birthdate in the format YYYY-MM-DD.',
        }

