from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'favorite_animal']
        widgets = { #optional, but recommended for better control
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'favorite_animal': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = { #optional, to change the label text
            'name': 'First Name',
            'surname': 'Last Name',
            'favorite_animal': 'Favorite Animal',
        }

