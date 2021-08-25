from django.contrib import admin
from theatres.models import Theatre, Seat, Runs_on
# Register your models here.

admin.site.register((Theatre, Seat, Runs_on, ))
