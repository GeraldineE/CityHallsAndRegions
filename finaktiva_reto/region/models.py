from uuid import uuid4
from django.db import models
from city_hall.models import CityHall


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code = models.CharField(max_length=11)
    name = models.CharField(max_length=200)
    city_halls = models.ManyToManyField(CityHall, related_name="regions", blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Region:{self.name}>"
