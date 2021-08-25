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


class CityList(generics.ListAPIView):
    queryset = models.Theatre.objects.all()
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
