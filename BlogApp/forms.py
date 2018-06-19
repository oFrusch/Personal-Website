from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'post', 'date_added', 'img']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.TextInput(attrs={'class': 'form-control'}),
            'date_added': forms.TextInput(attrs={'class': 'form-control'})
        }
