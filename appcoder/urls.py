from django.urls import path
from appcoder import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('proyectos_ley/', views.proyectos_Ley, name= 'Proyectos_Ley'),
    path('integrantes_proyecto/', login_required(views.integrantes_proyect), name= 'Integrantes_proyect' ),
    path('camara/', views.camara, name= 'Camara'),
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
    path('integrantes/list', login_required(views.IntegrantesList.as_view()), name='List'),
    path('<int:pk>/', login_required(views.IntegrantesDetalle.as_view()), name='Detalle'),
    path('nuevo/<int:pk>/', login_required(views.IntegrantesCreacion.as_view()), name='New'),
    path('editar/<int:pk>/', login_required(views.IntegrantesUpdate.as_view()), name='Edit'),
    path('borrar/<int:pk>/', login_required(views.IntegrantesDelete.as_view()), name='Delete'),
    path('login/', views.login_request, name='Login'),
    path('signup', views.register, name='Signup'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('edit/', views.edit , name= 'Edit'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail')
    ]
    #path('cambiar_pass/', views.CambiarPasswordView.as_view(), name='CambiarPass'),
