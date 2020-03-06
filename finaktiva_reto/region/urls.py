from django.urls import path
from .views import (
    RegionCreate,
    RegionList,
    RegionDetail,
    RegionUpdate,
    RegionDelete,
)

urlpatterns = [
    path("add/", RegionCreate.as_view(), name="region-create"),
    path("", RegionList.as_view(), name="region-list"),
    path("<uuid:pk>/", RegionDetail.as_view(), name="region-detail"),
    path("<uuid:pk>/change/", RegionUpdate.as_view(), name="region-update"),
    path("<uuid:pk>/delete/", RegionDelete.as_view(), name="region-delete"),
]
