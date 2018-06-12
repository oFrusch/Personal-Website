from django.shortcuts import render, get_object_or_404
from .models import Album, Song


# Second+ arguments have to match '<str:album_page>/' parameter in path, which is set in urls.py

def index(request):
    all_albums = Album.objects.all()  # Gets all albums from DB
    context = {'all_albums': all_albums}
    return render(request, 'My_Songs/homepage.html', context)


# Display all songs - Not sure why 'all_songs' is needed as a parameter
def all_songs(request):
    all_albums = Album.objects.all()  # Get all albums
    return render(request, 'My_Songs/songs.html', {'all_albums': all_albums})


def album_page(request):
    all_albums = Album.objects.all()  # Gets all albums from DB
    return render(request, 'My_Songs/album_page.html', {'all_albums': all_albums})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)  # Tries to get album based on id - If not found sends 404 Not Found
    return render(request, 'My_Songs/detail.html', {'album': album})


# Not currently being used - just an example of how to generate forms - Would need to add code back to detail.html (Video 24 in tutorials)
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
