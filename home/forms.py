from django import forms
from .models import News_letter


class NewsLetterForm(forms.ModelForm):
    """
    form for creating orders
    """
    class Meta:
        model = News_letter
        fields = (
            'full_name', 'email',
        )
