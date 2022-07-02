from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('about', views.about, name='about' ),
    path('mood_table', views.mood_table, name='mood'),

]
