from django.urls import path
import My_Songs.views



app_name = 'My_Songs'# Separate 'detail' 'index' and other patterns in between apps (My_Songs:detail)

urlpatterns = [
    # /My_Songs/
    path('', My_Songs.views.TemplateView.as_view(), name='index'),

    # /My_Songs/album_page/
    path('album_page/', My_Songs.views.AlbumView.as_view(), name='album_page'),

    # /My_Songs/<album_id>/
    path('<int:pk>/', My_Songs.views.DetailView.as_view(), name='detail'),

    # /My_Songs/all_songs/
    path('songs/', My_Songs.views.all_songs, name='all_songs'),


]
