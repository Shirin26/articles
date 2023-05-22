from django import forms
from django.forms import widgets

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Title')
    content = forms.CharField(max_length=3000, required=True, label='Content')
    author = forms.CharField(max_length=50, required=True, label='Author', widget=widgets.Textarea(attrs={'cols': 20, 'rows': 3}))