from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import authenticated_user,unauthenticated_user
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import AlbumForm

# Create your views here.

# Just showing the use of HttpResponse
def home1(request):
    return HttpResponse('<h1>This is your music website</h1>')

def arrange(artists):
    artist1,artist2=[],[]
    i=0
    for artist in artists:
        if i!=3:
            artist1.append(artist)
            i+=1
        else:
            artist2.append(artist1)
            i=0
            artist1=[]
            artist1.append(artist)
    artist2.append(artist1)
    return artist2

@unauthenticated_user
def home(request):
    albums=Album.objects.all()
    artists=Artist.objects.all()
    artist2=arrange(artists)
    songs=Song.objects.all()
    context={'albums':albums,'artist2':artist2,'songs':songs}
    return render(request,'music/home.html',context)

@login_required(login_url='login')
def artistdetail(request,pk):
    artist=Artist.objects.get(id=pk)
    songs=artist.song_set.all()
    context={'artist':artist,'songs':songs}
    return render(request,'music/artist.html',context)

@login_required(login_url='login')
def songdetail(request,pk):
    song=Song.objects.get(id=pk)
    context={'song':song}
    return render(request,'music/song.html',context)

@login_required(login_url='login')
def userhome(request):
    album=request.user.album
    artists=Artist.objects.all()
    artist2=arrange(artists)

    context={'album':album,'artist2':artist2}
    return render(request,'music/userhome.html',context)


@login_required(login_url='login')
def userpage(request):
    artists=request.user.album.artist_set.all()
    total=artists.count()
    context={'artists':artists,'total':total}
    return render(request,'music/user.html',context)

# @login_required(login_url='login')
# def songdetail(request):


@login_required(login_url='login')
def account_setting(request):
    user=request.user.album
    form=AlbumForm(instance=user)
    if request.method=='POST':
        form=AlbumForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'music/account_setting.html',context)

def playlist(request,pk):
    album=Album.objects.get(id=pk)
    artists=album.artist_set.all()
    songs=[]
    for artist in artists:
        songs.append(artist.song_set.all())
    context={'album':album,'artists':artists,'songs':songs}
    return render(request,'music/playlist.html',context)

def createplaylist(request,pk):
    songs=Song.objects.all()
    album1=Album.objects.get(id=pk)
    if request.method=='POST':
        songlist=request.POST.getlist('songlist')
        print("Songlist",songlist)
        artists=[]
        # artist=request.user.song.objects.filter(artist__name)
        for song in songlist:
            songobject=Song.objects.get(name=song)
            artists.append(Artist.objects.get(name=songobject.artist))
        print("Artists",artists)
        for artist in artists:
            artist.album.add(album1)
        return redirect('playlist',pk=album1.id)

    context={'songs':songs}
    return render(request,'music/createplaylist.html',context)

@authenticated_user
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            Album.objects.create(
                user=user,
                name=user.username,
            )
            print(user)
            print(username)
            messages.success(request,'Account was created for'+username)
            return redirect('login')
    context={'form':form}
    return render(request,'music/register.html',context)


@authenticated_user
def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,'username or password in incorrect')
            return redirect('login')
    else:
        return render(request,'music/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')