from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from django.shortcuts import render


def index(request):
    return render(request,'core/index.html')

#sacar todos los datos ingresados a mensaje para luego mostrarlos en proyectos.html
def listar(request):
        lista_proyectos= Mensaje.objects.all()
        data={
             "lista_proyectos": lista_proyectos,
        }
        
        return render(request,'core/proyectos.html',data)

@login_required
def home_view(request):
    return render(request, 'core/base.html')


   
def Sesion(request):
    if request.method == 'POST': #El usuario envía el formulario de inicio de sesión eso por el metodo post
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username, password=password)#verifica credenciales
        
        if user is not None:
            login(request, user)
            if  user.is_staff:
                return redirect('/proyectos')   #si son correctas y el usario es profesor redirecciona a proyectos
            else:
                 return redirect('/nuevo_proyecto') #si son correctas y el usuario es alumno redirecciona a ingresar un nuevo proyecto
        else:
            return render(request, 'core/proyectos.html')
    else:
        return render(request, 'core/login.html')
    
@login_required 
def logout_view(request):
        logout(request)
        return redirect('/InicioSesion')

def nuevo_proyecto(request):
    return render(request, 'core/nuevo_proyecto.html')


def agregar_proyecto(request):
        if(request.POST):
            nombre= request.POST['txtNombreproyecto']
            estudiante=request.POST['txtNombrestudiante']
            tipo= request.POST['cboTipo']
            profesor=request.POST['txtprofesor']
            informacion=request.POST['txtinformacion']            
            #validaciones 
                
            #se construye y se carga el objeto con los datos del form 
            mensaje=Mensaje()
            mensaje.Nombree=nombre
            mensaje.alumno=estudiante
            mensaje.tipo=tipo
            mensaje.profesor=profesor
            mensaje.informacion=informacion
            #guardar cambio en la base de datos
            mensaje.save()

        return render(request,'core/nuevo_proyecto.html')
def cuenta_con_patrocinio(request):
     lista_proyectos= Mensaje.objects.all()
     data={
             "lista_proyectos": lista_proyectos,
        }
     return render(request, 'core/Conpatrocinio.html', data)

def Ningun_patrocinio(request):
     lista_proyectos= Mensaje.objects.all()
     data={
             "lista_proyectos": lista_proyectos,
        }
     return render(request, 'core/SinPatrocinio.html', data)