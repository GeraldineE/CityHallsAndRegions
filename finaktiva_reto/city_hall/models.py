from uuid import uuid4
from django.db import models


class CityHall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code = models.CharField(max_length=11)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<CityHall:{self.name}>"

