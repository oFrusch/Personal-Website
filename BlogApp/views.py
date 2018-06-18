from BlogApp.models import BlogPost
from django.views import generic
from django.shortcuts import render


class BlogView(generic.ListView):
    template_name = 'Blog/all_posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return BlogPost.objects.all()


class PostView(generic.DetailView):
    model = BlogPost
    template_name = 'Blog/post.html'
    context_object_name = 'post'




