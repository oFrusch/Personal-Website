from django.urls import path
import BlogApp.views
from .views import NewBlogPostView

app_name = 'BlogApp'

urlpatterns = [

    # /BlogApp/
    path('', BlogApp.views.BlogView.as_view(), name='all_posts'),

    # /BlogApp/<post_id>/
    path('<int:pk>/', BlogApp.views.PostView.as_view(), name='post-detail'),

    path('new_post/', BlogApp.views.NewBlogPostView.as_view(), name='new_post'),

    path('<int:pk>/comment/', BlogApp.views.CommentCreate.as_view(), name='comment'),

]
