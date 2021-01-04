from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home,name='index'),

    path('comment/<int:id>/',views.comment,name="comment"),
    path('addcomment/',views.addcomment,name="addcomment"),
    path('editcomment/<int:id>',views.editcomment,name="editcomment"),
    path('editmovie/<int:id>/',views.edit,name="edit"),
    path('addmovie/', views.addmovie, name="add"),
    path('movies/', views.movies, name="movies"),
    path('movies/<int:id>/',views.movie,name="movie"),
]