from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare, name='compare'),
    path('search', views.search, name='search'),
]