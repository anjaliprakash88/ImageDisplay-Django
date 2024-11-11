from django import forms
from .models import ImageDisplay


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageDisplay
        fields = '__all__'