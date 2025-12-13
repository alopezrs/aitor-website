#from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    # Url inicial
    path('', views.index, name='index'),

    # Urls para experiencia
    path('trayectoria', views.ExperienciaListView.as_view(), name='trayectoria'),

    # Urls para educacion
    path('formacion', views.EducacionListView.as_view(), name='formacion'),

    # Urls para certificados
    path('certificados', views.CertificadoListView.as_view(), name='certificado'),
    path('certificado/<int:pk>', views.CertificadoDetailView.as_view(), name='certificado_detail'),

    # Url para contacto
    path('perfil', views.InfoListView.as_view(), name='perfil'),

    # Url para Login
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.UserLoginView.as_view(), name='logout'),
]