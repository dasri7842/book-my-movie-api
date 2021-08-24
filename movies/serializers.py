from django.db.models import fields
from rest_framework import serializers
from . import models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class CrewMemberSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='person.id')
    name = serializers.ReadOnlyField(source='person.name')
    image_link = serializers.ReadOnlyField(source='person.image_link')

    class Meta:
        model = models.CrewMember
        fields = ('id', 'name', 'image_link', 'role', 'role_name')


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    languages = LangSerializer(many=True)
    crew = CrewMemberSerializer(
        source='crewmember_set', many=True, read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'
