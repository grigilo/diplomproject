from django import forms

from ad.models import Ad
from common.views import StyleFormMixin


class AdForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'image', 'description', 'price')
