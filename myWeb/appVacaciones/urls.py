from django.urls import path
from . import views

urlpatterns = [
    # Url inicial
    path('', views.indexVacaciones, name='indexVacaciones'),
]