from django.db.models import fields
from rest_framework import serializers
from . import models


class GenreSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.genre

    class Meta:
        model = models.Genre
        fields = '__all__'


class LangSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.language

    class Meta:
        model = models.Language
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class CrewMemberSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='person.name')
    image_link = serializers.ReadOnlyField(source='person.image_link')

    class Meta:
        model = models.CrewMember
        fields = ('name', 'image_link', 'role', 'role_name')


class AddCrewMemSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    person_id = serializers.IntegerField()

    role = serializers.CharField()
    role_name = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        person = models.Person.objects.get(
            pk=int(validated_data.get('person_id')))
        movie = models.Movie.objects.get(
            pk=int(validated_data.get('movie_id')))
        crew_member = models.CrewMember.objects.create(
            person=person, movie=movie, role=validated_data['role'], role_name=validated_data['role_name'])

        crew_member.save()
        return crew_member


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    languages = LangSerializer(many=True)
    crew = CrewMemberSerializer(
        source='crewmember_set', many=True, read_only=True)

    def create(self, validated_data):
        genres = list(map(lambda item: item['genre'],
                          validated_data.pop('genres')))
        genres = models.Genre.objects.filter(genre__in=genres)

        languages = list(map(lambda item: item['language'],
                             validated_data.pop('languages')))
        languages = models.Language.objects.filter(language__in=languages)

        movie_instance = models.Movie.objects.create(**validated_data)
        movie_instance.save()

        for item in genres:
            movie_instance.genres.add(item)
        for item in languages:
            movie_instance.languages.add(item)

        return movie_instance

    class Meta:
        model = models.Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    languages = LangSerializer(many=True, read_only=True)
    crew = CrewMemberSerializer(
        source='crewmember_set', many=True, read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'
