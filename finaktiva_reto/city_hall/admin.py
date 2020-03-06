from django.contrib import admin
from .models import CityHall


@admin.register(CityHall)
class CityHallAdmin(admin.ModelAdmin):
    pass

