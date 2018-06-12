from django.urls import path
from . import views

app_name = 'My_Songs'# Separate 'detail' 'index' and other patterns in between apps (My_Songs:detail)

urlpatterns = [
    # /My_Songs/
    path('', views.index, name='index'),

    # /My_Songs/album_page/
    path('album_page/', views.album_page, name='album_page'),

    # /My_Songs/<album_id>/
    path('<int:album_id>/', views.detail, name='detail'),

    # /My_Songs/<album_id>/favorite/
    path('<int:album_id>/', views.favorite, name='favorite'),

    # /My_Songs/all_songs/
    path('songs/', views.all_songs, name='all_songs'),
]