from django.db import models
from django.db.models.deletion import DO_NOTHING
from theatres.models import Theatre, Show
# Create your models here.


class Seat(models.Model):
    seat_code = models.CharField(max_length=10)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)


class Ticket(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    seat_id = models.ForeignKey(Seat, on_delete=DO_NOTHING)
    email = models.EmailField(max_length=256)
    booking_time = models.DateTimeField()
