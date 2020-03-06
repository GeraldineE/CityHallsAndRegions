from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Region


class RegionCreate(CreateView):
    model = Region
    fields = "__all__"
    success_url = reverse_lazy("region-list")


class RegionList(ListView):
    model = Region
    context_object_name = "region_list"


class RegionDetail(DetailView):
    model = Region


class RegionUpdate(UpdateView):
    fields = "__all__"
    model = Region
    success_url = reverse_lazy("region-list")


class RegionDelete(DeleteView):
    model = Region
    success_url = reverse_lazy("region-list")

