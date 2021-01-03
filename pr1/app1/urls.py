from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home),

    path('addmovie', views.addmovie, name="add"),
    path('movies/', views.movies, name="movies"),
    path('movies/<int:id>/',views.movie,name="movie"),
]