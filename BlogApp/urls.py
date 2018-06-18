from django.urls import path
import BlogApp.views

app_name = 'BlogApp'

urlpatterns = [

    # /BlogApp/
    path('', BlogApp.views.BlogView.as_view(), name='all_posts'),

    # /BlogApp/<post_id>/
    path('<int:pk>/', BlogApp.views.PostView.as_view(), name='post-detail'),

]
