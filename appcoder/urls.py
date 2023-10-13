from django.urls import path
from appcoder import views

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('proyectos_ley/', views.proyectos_Ley, name= 'Proyectos_Ley'),
    path('integrantes_proyecto/', views.Integrantes_proyect,name= 'Integrantes_proyect' ),
    path('camara/', views.Camara, name= 'Camara'),
    path('fecha_inicio/', views.Fecha_Inicio, name= 'Fecha_Inicio'),
    path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'),
    path('integrantesFormulario', views.integrantesFormulario, name='IntegrantesFormulario'),
    path('camaraFormulario', views.camaraFormulario, name='CamaraFormulario'),
    path('busqueda_proyecto_form/', views.busqueda_proyecto_ley_form,
         name='busqueda_proyecto_ley'),
    path('busqueda_proyecto_ley/', views.busqueda_proyecto_ley,name='busqueda_proyecto_ley'),
    path('leerProyectos', views.leerProyectos, name='LeerProyectos'),
    path('delete_proyecto/<int:proyecto_id>/', views.delete_proyecto, name='DeleteProyecto'),
    path('edit_proyecto/<int:proyecto_id>/', views.edit_proyecto, name='EditProyecto'),
    path('proyecto/list', views.ProyectoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProyectoDetalle.as_view(), name='Detalle'),
    path(r'^nuevo$', views.ProyectoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProyectoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProyectoDelete.as_view(), name='Delete')

    ]
