from django import forms
from . import models


class BoardForm(forms.ModelForm):
    title = forms.CharField(max_length=15)
    content = forms.CharField(max_length=100)
    class Meta:
        model = models.Board
        fields = ('title', 'content', 'create_at', )

class CateForm(forms.ModelForm):
    class Meta:
        model = models.Cate
        fields = ('cate', )

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=100)
    class Meta:
        model = models.Comment
        fields = ('content', 'create_at',)