from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare, name='compare1'),
    path('data', views.AjaxHandlerView.as_view())
]