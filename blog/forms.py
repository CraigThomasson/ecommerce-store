from django import forms
from .models import Blog

class Blog_form(forms.ModelForm):
    """
    form for managing crud for blogs
    """
    class Meta:
        model = Blog
        fields = '__all__'