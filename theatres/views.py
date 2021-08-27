from django.shortcuts import render

from rest_framework import generics
from . import models, serializers
# Create your views here.


class TheatreList(generics.ListCreateAPIView):
    queryset = models.Theatre.objects.all()
    serializer_class = serializers.TheatreSerializer


class TheatreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Theatre.objects.all()
    serializer_class = serializers.TheatreSerializer


class ShowList(generics.ListAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializer


class ShowDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializer


class CreateShow(generics.ListCreateAPIView):
    serializer_class = serializers.AddShowSerializer


class CityList(generics.ListAPIView):
    queryset = models.Theatre.objects.order_by(
        'city').values_list('city', flat=True).distinct('city')
    serializer_class = serializers.CitySerializer


class Runs_OnList(generics.ListAPIView):
    queryset = models.Runs_on.objects.all()
    serializer_class = serializers.Runs_onSerializer


class Runs_OnCreate(generics.CreateAPIView):
    serializer_class = serializers.AddRuns_OnSerializer


class Runs_OnDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Runs_on.objects.all()
    serializer_class = serializers.Runs_OnDetailSerializer


class CityMovieList(generics.ListAPIView):
    serializer_class = serializers.CityMovieSerializer

    def get_queryset(self):
        return models.Runs_on.objects.filter(theatre__city=self.kwargs['city'])


class TheatreShows(generics.ListAPIView):
    serializer_class = serializers.TheatreShowsSerializer

    def get_queryset(self):
        params = self.request.query_params
        filters = {}
        filters['theatre__city'] = self.kwargs['city']
        filters['shows__movie__movie_id'] = self.kwargs['movie']
        filters['shows__language'] = params['language']
        filters['shows__show_date'] = params['show_date']
        return models.Runs_on.objects.filter(**filters)

    def get_serializer_context(self):
        nested_filters = {}
        params = self.request.query_params
        nested_filters['movie__movie_id'] = self.kwargs['movie']
        nested_filters['language'] = params['language']
        nested_filters['show_date'] = params['show_date']
        return {'filters': nested_filters}
