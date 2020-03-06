from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import CityHall


class CityHallCreate(CreateView):
    model = CityHall
    fields = ["__all__"]
    success_url = reverse_lazy("city-hall-list")


class CityHallList(ListView):
    model = CityHall


class CityHallDetail(DetailView):
    model = CityHall


class CityHallUpdate(UpdateView):
    model = CityHall


class CityHallDelete(DeleteView):
    model = CityHall
    success_url = reverse_lazy("city-hall-list")

