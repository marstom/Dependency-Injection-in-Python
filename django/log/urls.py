

from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.logs_list),
]
