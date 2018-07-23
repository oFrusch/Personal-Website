from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'post', 'date_added', 'img']


class CommentPostForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']


