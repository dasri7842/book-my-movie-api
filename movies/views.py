from django.shortcuts import render
from rest_framework import generics

# Create your views here.

from movies.models import Genre, Language, Movie, Person
from movies.serializers import AddCrewMemSerializer, GenreSerializer, LangSerializer, MovieDetailSerializer, MovieSerializer, PersonSerializer


############### MOVIE #################


class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        params = self.request.query_params
        filter_params = {
            'genre': 'genres__genre__in',
            'lang': 'languages__language__in',
            'crew': 'crew__crewmember__person__name__in'
        }
        filter_kwargs = {}
        for key in filter_params:
            if key in params:
                filter_kwargs[filter_params[key]] = params[key].replace(
                    '%20', ' ').split(',')

        return Movie.objects.filter(**filter_kwargs)


class MoiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class TopMovies(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        count = self.request.query_params.get('count')
        if count and count.isnumeric():
            return Movie.objects.all().order_by('-rating')[:int(count)]
        return Movie.objects.all().order_by('-rating')[:5]


############### Crew #################

class AddCrewMemember(generics.CreateAPIView):
    serializer_class = AddCrewMemSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


############## Genre ##################


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

############## Language ###############


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LangSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LangSerializer
