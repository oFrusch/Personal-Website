from BlogApp.models import BlogPost
from django.views import generic
from django.shortcuts import render
from .forms import BlogPostForm


class BlogView(generic.ListView):
    template_name = 'Blog/all_posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return BlogPost.objects.order_by('-id')


class PostView(generic.DetailView):
    model = BlogPost
    template_name = 'Blog/post.html'
    context_object_name = 'post'


def new_post(request):
    template = 'Blog/new_post.html'
    form = BlogPostForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        form = BlogPostForm()

    context = {
        'form': form,
    }
    return render(request, template, context)
