from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'favorite_number']
        widgets = { #optional, but recommended for better control
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'favorite_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = { #optional, to change the label text
            'name': 'First Name',
            'surname': 'Last Name',
            'favorite_number': 'Favorite Number',
        }

    def clean_favorite_number(self): #Example of custom validation
        favorite_number = self.cleaned_data['favorite_number']
        if favorite_number < 0:
            raise forms.ValidationError("Favorite number cannot be negative.")
        return favorite_number
