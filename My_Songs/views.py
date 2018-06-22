from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Second+ arguments have to match '<str:album_page>/' parameter in path, which is set in urls.py

class TemplateView(generic.TemplateView):
    template_name = 'My_Songs/homepage.html'


# Display all songs - Not sure why 'all_songs' is needed as a parameter
def all_songs(request):
    all_albums = Album.objects.all()  # Get all albums
    return render(request, 'My_Songs/songs.html', {'all_albums': all_albums})


class AlbumView(generic.ListView):
    template_name = 'My_Songs/album_page.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'My_Songs/detail.html'


class SongCreate(CreateView):
    model = Song
    context_object_name = 'song'
    fields = ['album', 'song_title', 'song_link', 'song_description']


class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'song_link', 'song_description']


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('My_Songs:index')

