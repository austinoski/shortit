from unicodedata import name
from django.urls import path

from .views import HomeView, DetailView, RedirectView


urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("<str:key>/detail", DetailView.as_view(), name="detail"),
    path("<str:key>", RedirectView.as_view(), name="redirect"),
]
