from django.urls import path
from .views import create, create1


urlpatterns = [
    path('create/', create),
    path('all/', create1)
    ]