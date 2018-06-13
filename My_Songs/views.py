from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views import generic


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


# Not currently being used - just an example of how to generate forms
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)  # Tries to get album based on id - If not found sends 404 Not Found
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'My_Songs/detail.html', {
            'album':album,
            'error_message':"Not a valid song"
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'My_Songs/detail.html', {'album': album})
