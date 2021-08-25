from django.db.models import fields
from rest_framework import serializers
from . import models
from movies.models import Movie
from movies.serializers import MovieMinDetailSerializer


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theatre
        fields = '__all__'


class SeatSearializer(serializers.ModelSerializer):
    theatre = TheatreSerializer(read_only=True)

    class Meta:
        model = models.Seat
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theatre
        fields = ('city',)

    def to_representation(self, instance):
        return instance.city


class Runs_onSerializer(serializers.ModelSerializer):
    theatre = TheatreSerializer()
    movie = MovieMinDetailSerializer()

    class Meta:
        model = models.Runs_on
        fields = '__all__'


class AddRuns_OnSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    theatre_id = serializers.IntegerField()
    language = serializers.CharField()
    show_date = serializers.DateField()
    show_time = serializers.TimeField()

    def create(self, validated_data):
        try:
            validated_data['movie'] = Movie.objects.get(
                pk=int(validated_data.pop('movie_id')))
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        try:
            validated_data['theatre'] = models.Theatre.objects.get(
                pk=int(validated_data.pop('theatre_id')))
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        try:
            instance = models.Runs_on.objects.create(**validated_data)
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        return instance


class Runs_OnDetailSerializer(serializers.ModelSerializer):
    theatre = TheatreSerializer(read_only=True)
    movie = MovieMinDetailSerializer(read_only=True)

    class Meta:
        model = models.Runs_on
        fields = '__all__'


class CityMovieSerializer(serializers.ModelSerializer):
    movie = MovieMinDetailSerializer(read_only=True)

    class Meta:
        model = models.Runs_on
        fields = ('movie',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data.get('movie')
