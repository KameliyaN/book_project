from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_pages(self):
        pages = self.cleaned_data['pages']

        if pages <= 0:
            raise ValidationError('Pages should be more than zero')
        if not isinstance(pages, int):
            raise ValidationError('Pages must be a number!')
        return pages

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title[0].isupper():
            raise ValidationError('The title must starts with capital letter')
        return title
