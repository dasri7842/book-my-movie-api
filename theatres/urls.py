from theatres.views import TheatreList
from django.urls import path
from theatres import views

urlpatterns = [
    path('theatre/', views.TheatreList.as_view()),
    path('theatre/<int:pk>/', views.TheatreDetail.as_view()),
    path('cities/', views.CityList.as_view()),
    path('cities/<str:city>/movies/', views.CityMovieList.as_view()),
    path('movie/runs_on/', views.Runs_OnList.as_view()),
    path('movie/runs_on/new', views.Runs_OnCreate.as_view()),
    path('movie/runs_on/<int:pk>/', views.Runs_OnDetail.as_view())
]
