from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Not valid extension')
        return url

    def save(self, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # download the image
        response = request.urlopen(url)
        image.image.save(image_name, ContentFile(response.read())
                         , save=False)

        if commit:
            image.save()
        return image
