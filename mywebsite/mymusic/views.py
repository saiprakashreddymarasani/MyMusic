from django.shortcuts import render
from django.http import Http404
from .models import Album,Song
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):
    all_albums = Album.objects.all()

    return render(request,'mymusic/index.html',{"all_albums": all_albums})

def detail(request,album_id):
    #try:
    #   album=Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #   raise Http404("Album doses not exist")
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'mymusic/detail.html',{"album" : album})

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request, 'mymusic/detail.html',
                      {"album": album},
                      {'erroe_message': 'you didnt select a valid song'},)
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request, 'mymusic/detail.html', {"album": album})

