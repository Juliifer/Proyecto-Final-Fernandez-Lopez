from django.urls import path
from appcoder import views
from django.contrib.auth.views import LogoutView

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
    path('integrantes/list', views.IntegrantesList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.IntegrantesDetalle.as_view(), name='Detalle'),
    path('vista/nuevo/', views.IntegrantesCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.IntegrantesUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.IntegrantesDelete.as_view(), name='Delete'),
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    #path('editarPerfil/', views.editarPerfil, name='EditarPerfil'),
    #path('cambiar_pass/', views.CambiarPasswordView.as_view(), name='CambiarPass'),
    
    ]
