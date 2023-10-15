from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.register, name='signup'),
]
