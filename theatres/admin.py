from django.contrib import admin
from theatres.models import Show, Theatre, Runs_on
# Register your models here.

admin.site.register((Theatre, Runs_on, Show))
