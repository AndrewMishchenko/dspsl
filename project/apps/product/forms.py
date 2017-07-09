from django.forms import ModelForm

from .models import (ProductComments,
                     ProductLikes
                     )


class LikesForm(ModelForm):
    class Meta:
        model = ProductLikes
        fields = ['product']


class CommentForm(ModelForm):
    class Meta:
        model = ProductComments
        fields = ['text', 'product']
