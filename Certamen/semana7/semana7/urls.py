"""
URL configuration for semana7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),#django
    path('', views.index, name="home"),#la pagina inicial
    path('proyectos/', views.listar, name="proyectos"), #muestra datos de los proyectos
    path('InicioSesion/', views.Sesion, name="iniciarsesion"),#el login
    path('logout/', views.logout_view, name='logout'), #para deslogearse
    path('nuevo_proyecto/', views.nuevo_proyecto, name="nuevo_proyecto"),#para crear un proyecto
    path('agregar_proyecto/', views.agregar_proyecto, name="agregar_proyecto"),#para guardar los datos de proyectos
    path('Patrocinio/', views.cuenta_con_patrocinio, name="ConPatrocinio"),
    path('NingunPatrocinador/', views.Ningun_patrocinio, name="NingunPatrocinador"),
]
