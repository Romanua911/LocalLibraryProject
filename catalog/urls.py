from django.urls import path, include
from . import views


# Add admin path
urlpatterns = [
    path('', views.index, name='index'),
]
