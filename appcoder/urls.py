from django.urls import path
from .views import inicio, Proyectos_Ley, Integrantes_proyect, Camara, Fecha_Inicio

urlpatterns = [
    path('index/',inicio), #esta era nuestra primer view
    path('proyectos_ley', Proyectos_Ley),
    path('integrantes_proyecto', Integrantes_proyect),
    path('camara', Camara),
    path('fecha_inicio', Fecha_Inicio),
]
