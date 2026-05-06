from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок записи...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваши мысли...', 'rows': 10}),
        }