from django import forms


from comments.models import Comment
from common.views import StyleFormMixin


class CommentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
