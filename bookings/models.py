from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from theatres.models import Theatre, Show
# Create your models here.


class Seat(models.Model):
    seat_code = models.CharField(max_length=10)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['seat_code', 'theatre', 'show'], name='Seat for a show')
        ]


class Ticket(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    seats = models.ManyToManyField(Seat)
    email = models.EmailField(max_length=256)
    booking_time = models.DateTimeField(auto_now=True)
