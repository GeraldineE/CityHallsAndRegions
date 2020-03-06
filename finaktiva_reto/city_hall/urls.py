from django.urls import path
from .views import (
    CityHallCreate,
    CityHallList,
    CityHallDetail,
    CityHallUpdate,
    CityHallDelete,
)

urlpatterns = [
    path("add/", CityHallCreate.as_view(), name="city-hall-create"),
    path("", CityHallList.as_view(), name="city-hall-list"),
    path("<uuid:pk>/", CityHallDetail.as_view(), name="city-hall-detail"),
    path("<uuid:pk>/change/", CityHallUpdate.as_view(), name="city-hall-update"),
    path("<uuid:pk>/delete/", CityHallDelete.as_view(), name="city-hall-delete"),
]
