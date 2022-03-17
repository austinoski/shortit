from unicodedata import name
from django.urls import path

from .views import HomeView, DetailView


urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("<str:key>/detail", DetailView.as_view(), name="detail"),
]
