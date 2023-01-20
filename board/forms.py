from django import forms
from . import models


class BoardForm(forms.ModelForm):
    title = forms.CharField(max_length=15)
    content = forms.CharField(max_length=100)
    class Meta:
        model = models.Board
        fields = ('title', 'content', )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('category', )

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=100)
    class Meta:
        model = models.Comment
        fields = ('content',)