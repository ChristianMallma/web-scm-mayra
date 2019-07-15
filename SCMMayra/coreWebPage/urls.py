from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('homePage/',Home.as_view(),name="homePage"),
]