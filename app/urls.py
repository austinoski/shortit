from unicodedata import name
from django.urls import path

from .views import HomeView, RedirectView


urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("<str:key>", RedirectView.as_view(), name="redirect"),
]
