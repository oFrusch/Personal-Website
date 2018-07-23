from BlogApp.models import BlogPost
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import BlogPostForm, CommentPostForm
from django.views.generic.edit import CreateView
from .models import Comment


class BlogView(generic.ListView):
    template_name = 'Blog/all_posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return BlogPost.objects.order_by('-id')


class PostView(generic.DetailView):
    model = BlogPost
    template_name = 'Blog/post.html'
    context_object_name = 'post'


class NewBlogPostView(View):
    template_name = 'Blog/new_post.html'
    form_class = BlogPostForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('BlogApp:all_posts')

        return render(request, self.template_name, {'form': form})


class CommentCreate(CreateView):
    template_name = "Blog/comment_form.html"
    model = Comment
    context_object_name = 'comment'
    fields = ['post','comment']





    # if form.is_valid():
    #     form.save()
    # else:
    #     form = BlogPostForm()
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, template, context)
