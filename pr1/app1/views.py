from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from.models import Movie,Comment
from .forms import CommentForm,CreateUserForm,MovieForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

@permission_required('app1.edit_comment')
def editcomment(request, id):
    comment = Comment.objects.get(id = id)
    form = CommentForm(instance = comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'addcomment.html', context)

@permission_required('app1.edit_movie')
def edit(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(instance = movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'addmovie.html',context)

@login_required
def movies(request):
    tmp = Movie.objects.all()
    return render(request, 'movies.html', {'movies': tmp})

@login_required
def movie(request, id):
    comments = []
    tmp = get_object_or_404(Movie, id=id)
    comments = Comment.objects.all()
    komentari = []
    for kom in comments:
        if kom.movie_id == id:
            komentari.append(kom)

    return render(request,'movie.html',{'movie':tmp, 'page_title':tmp.movieName, 'comments':komentari})

@login_required
def comments(request):
    tmp = Comment.objects.all()
    return render(request,'comments.html',{'comments': tmp})

@login_required
def comment(request,id):
    tmp = get_object_or_404(Comment, id = id)
    return render(request,'comment.html',{'comment':tmp})

@permission_required('app1.add_movie')
def addmovie(request):
    form = MovieForm(request.POST)
    if form.is_valid():
        mov = Movie(movieName=form.cleaned_data['movieName'], rating=form.cleaned_data['rating'], owner= request.user)
        mov.save()

    context={'form':form}
    return render(request,'addmovie.html',context)

@permission_required('app1.add_comment')
def addcomment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comm = Comment(movie=form.cleaned_data['movie'] ,content=form.cleaned_data['content'],owner = request.user)
        comm.save()

    context={'form':form}
    return render(request,'addcomment.html',context)

@login_required
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
            return redirect('app1:index')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def indexpage(request):
    return render(request, 'index.html')