from django.contrib import admin

from . import models
# Register your models here.
admin.site.register([models.Movie, models.Person,
                    models.Language, models.Genre, models.CrewMember])
