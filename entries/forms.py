from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Entry


class EntryForm(forms.ModelForm):
    """Форма для записи"""
    class Meta:
        model = Entry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок записи...'
            }),
            'content': CKEditor5Widget(
                config_name='default',
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = 'Содержание'