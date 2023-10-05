from django.urls import path
from appcoder import views

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('proyectos_ley', views.Proyectos_Ley, name= 'Proyectos de Ley'),
    path('integrantes_proyecto', views.Integrantes_proyect,name= 'Integrantes del proyecto' ),
    path('camara', views.Camara, name= 'Camara'),
    path('fecha_inicio', views.Fecha_Inicio, name= 'Fecha_Inicio'),]
