from django.urls import path
from appcoder import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('proyectos_ley/', views.proyectos_Ley, name= 'Proyectos_Ley'),
    path('integrantes_proyecto/', login_required(views.integrantes_proyect), name= 'Integrantes_proyect' ),
    path('camara/', views.camara, name= 'Camara'),
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
    path('login/', views.login_request, name='Login'),
    path('signup', views.register, name='Signup'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('edit/', views.edit , name= 'Edit'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('blog/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/send/', views.send_message, name='send_message')
    ]
    #path('cambiar_pass/', views.CambiarPasswordView.as_view(), name='CambiarPass'),
