from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from.models import Movie,Comment
from .forms import CreateUserForm,MovieForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def movies(request):
    tmp = Movie.objects.all()
    return render(request, 'movies.html', {'movies': tmp})

def movie(request, id):
    tmp = get_object_or_404(Movie, id=id)
    return render(request,'movie.html',{'movie':tmp, 'page_title':tmp.movieName})

def addmovie(request):
    form = MovieForm(request.POST)
    if form.is_valid():
        mov = Movie(movieName=form.cleaned_data['movieName'], rating=form.cleaned_data['rating'], owner= request.user)
        mov.save()
    context={'form':form}
    return render(request,'addmovie.html',context)

def home(request):
    return render(request, 'dashboard.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('app1:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def indexpage(request):
    return render(request, 'index.html')