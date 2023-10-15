from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.registro, name='signup'),

]
