from django import forms
from .models import Book

# class addBookForm(forms.Form):
#     title = forms.CharField(label='title', max_length=100)
#     author = forms.CharField(label='author', max_length=100)
#     published_year = forms.IntegerField(label='published_year')
#     genre = forms.CharField(label='genre', max_length=30)

class addBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'genre']