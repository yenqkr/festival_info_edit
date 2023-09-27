from django import forms
from .models import Info, InfoImage
from django.forms import modelformset_factory

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'content', 'images']
    
    images = forms.FileField(required=False)

    def clean_images(self):
        images = self.cleaned_data.get('images')
        num_images = len(images) if isinstance(images, list) else 1
        if num_images > 10:
            raise forms.ValidationError("You can't upload more than 10 images.")
        return images