from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class Forms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titles','category','content','image','draft']
    def clean_titles(self):

        titles=self.cleaned_data['titles']


        if titles.isdigit():
            raise forms.ValidationError("zehmet olmasa herflerden ibaret deyer elave edin")
        return titles
