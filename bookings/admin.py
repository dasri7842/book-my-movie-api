from django.contrib import admin
from bookings.models import Seat, Ticket
# Register your models here.

admin.site.register([Seat, Ticket])
