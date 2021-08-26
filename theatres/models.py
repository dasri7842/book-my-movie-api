from django.db import models
from movies.models import Movie

# Create your models here.


class Theatre(models.Model):
    theatre_id = models.BigAutoField(primary_key=True)
    screen_name = models.CharField(max_length=100)
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256, default='stree_name')
    city = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name + ' ' + self.screen_name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.CharField(max_length=100, default='English')
    show_date = models.DateField()
    show_time = models.TimeField()
    price = models.IntegerField(default=100)

    def __str__(self) -> str:
        return '{} in {} at {}'.format(self.movie, self.language, self.show_time)


class Runs_on(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    shows = models.ManyToManyField(Show)

    def __str__(self) -> str:
        return '{} in {}'.format('Shows', self.theatre)
