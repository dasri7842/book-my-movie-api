from django.urls import path
from movies import views

urlpatterns = [
    path('genre/', views.GenreList.as_view()),
    path('genre/<int:pk>/', views.GenreDetail.as_view()),

    path('lang/', views.LanguageList.as_view()),
    path('lang/<int:pk>/', views.LanguageDetail.as_view()),

    path('person/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),

    path('movie/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MoiveDetail.as_view()),
    path('movie/top/', views.TopMovies.as_view()),
    path('movie/add_crew/', views.AddCrewMemember.as_view())
]
