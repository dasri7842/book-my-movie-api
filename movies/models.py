from django.db import models

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class Person(models.Model):
    name = models.CharField(max_length=128)
    image_link = models.URLField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    rating = models.DecimalField(decimal_places=3, max_digits=5)
    certification = models.CharField(max_length=100)
    duration = models.IntegerField()
    release_date = models.DateField()
    about = models.CharField(max_length=256)
    poster_link = models.URLField()
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    crew = models.ManyToManyField(Person, through='CrewMember')

    def __str__(self):
        return self.title


class CrewMember(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    role_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = [['person', 'movie']]

    def __str__(self) -> str:
        return self.role_name
