from django.db.models import fields
from rest_framework import serializers
from . import models
from movies.models import Movie
from movies.serializers import MovieMinDetailSerializer


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theatre
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):
    movie = MovieMinDetailSerializer(read_only=True)

    class Meta:
        model = models.Show
        fields = '__all__'


class AddShowSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField()

    class Meta:
        model = models.Show
        exclude = ('movie', )

    def create(self, validated_data):
        try:
            movie = Movie.objects.get(pk=validated_data['movie_id'])
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        validated_data['movie'] = movie
        try:
            show = models.Show.objects.create(**validated_data)
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        return show


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theatre
        fields = ('city',)

    def to_representation(self, instance):
        return instance.city


class MinifiedShowSerializer(serializers.ModelSerializer):
    movie = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = models.Show
        fields = ('movie', 'show_date', 'show_time', 'price')


class Runs_onSerializer(serializers.ModelSerializer):
    shows = MinifiedShowSerializer(many=True, read_only=True)

    class Meta:
        model = models.Runs_on
        fields = '__all__'


class AddRuns_OnSerializer(serializers.Serializer):
    theatre_id = serializers.IntegerField(write_only=True)
    show_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Runs_on
        exclude = ('theatre_id', 'show_id', )

    def create(self, validated_data):
        try:
            theatre_item = models.Theatre.objects.get(
                pk=int(validated_data.pop('theatre_id')))
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        try:
            show_item = models.Show.objects.get(
                pk=int(validated_data.pop('show_id')))
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        try:
            instance = models.Runs_on.objects.create(theatre=theatre_item)
            instance.save()
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        try:
            instance.shows.add(show_item)
            instance.save()
        except Exception as err_msg:
            raise serializers.ValidationError(err_msg)

        return instance


class Runs_OnDetailSerializer(serializers.ModelSerializer):
    theatre = TheatreSerializer(read_only=True)
    shows = MinifiedShowSerializer(many=True, read_only=True)

    class Meta:
        model = models.Runs_on
        fields = '__all__'


class ShowMovieSerializer(serializers.ModelSerializer):
    movie = MovieMinDetailSerializer()

    class Meta:
        model = models.Show
        fields = ('movie',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret.get('movie')


class CityMovieSerializer(serializers.ModelSerializer):
    shows = ShowMovieSerializer(many=True, read_only=True)

    class Meta:
        model = models.Runs_on
        fields = ('shows',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret.get('shows')


class ListFilterShowsSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(**self.context['filters'])
        return super().to_representation(data)


class FilterShowsSerializer(serializers.ModelSerializer):
    # movie = MovieMinDetailSerializer()

    class Meta:
        model = models.Show
        list_serializer_class = ListFilterShowsSerializer
        fields = ('show_time', 'price', 'show_date', 'id')


class TheatreShowsSerializer(serializers.ModelSerializer):
    shows = FilterShowsSerializer(many=True, read_only=True)
    theatre = TheatreSerializer(read_only=True)

    class Meta:
        model = models.Runs_on
        exclude = ('id',)
