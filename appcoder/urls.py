from django.urls import path
from appcoder import views

urlpatterns = [
    path('', views.inicio), #esta era nuestra primer view
    path('proyectos de ley', views.Proyectos_Ley),
    path('integrantes del proyecto', views.Integrantes_proyect),
    path('camara que conforma', views.Camara),
    path('fecha inicio proyecto', views.Fecha_Inicio),
]
