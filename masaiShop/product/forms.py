from django import forms
from .models import Comment

class CommentForm(forms.Media):
    class Meta:
        model = Comment
        fields = ['description']