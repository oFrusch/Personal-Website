from django.urls import path
from . import views

app_name = 'My_Songs'# Separate 'detail' 'index' and other patterns in between apps (My_Songs:detail)

urlpatterns = [
    # /My_Songs/
    path('', views.TemplateView.as_view(), name='index'),

    # /My_Songs/album_page/
    path('album_page/', views.AlbumView.as_view(), name='album_page'),

    # /My_Songs/<album_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /My_Songs/<album_id>/favorite/
    path('<int:album_id>/', views.favorite, name='favorite'),

    # /My_Songs/all_songs/
    path('songs/', views.all_songs, name='all_songs'),
]