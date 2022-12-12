from django import forms
from .models import *


class AddPostFrom(forms.ModelForm):
    class Meta:
        model = Guns
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'from-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows':10})
        }

