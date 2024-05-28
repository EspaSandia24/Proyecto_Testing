from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from inicio.models import Equipo, OrdenServicio
from django.contrib.auth.models import User,Group
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse


from inicio.forms import FormEquipo, FormServicio, FormEditarOrden, FormEditarEquipo


# Create your views here.

# Create your views here.

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    
@login_required
def registrar(request):
    usuario_guardado = None  # Inicializar como una instancia vacía
    if request.method == 'POST':
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        email = None
        verificar_password = request.POST.get('password2')

        if password == verificar_password:

             # Verificar si el usuario ya existe en la base de datos
            if User.objects.filter(username=usuario).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
                return render(request, 'register.html')
            
            user = User.objects.create_user(username=usuario, email=email, password=password)
            user.groups.add(Group.objects.get(name='Empleado'))
            user.save()
            return redirect('Principal') 
                
    return render(request, 'usuarios/register.html')

@login_required
def incio(request):
    return render(request, 'index.html')

@login_required
def lista_equipos(request):
    context={
        'equipo': Equipo.objects.all()
    }
    return render(request, 'equipos/lista_equipos.html',context)

@login_required
def agregar_equipo(request):
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Equipos')
    else:
        form = FormEquipo()
            
    context = {
        'form' : form
    }     
    return render(request, 'equipos/nuevo_equipo.html', context)

@login_required
def lista_servicios(request):
    
    context={
        'servicio': OrdenServicio.objects.all()
    }
    return render(request, 'servicios/lista_servicios.html',context)

@login_required
def agregar_servicio(request):
    if request.method == 'POST':
        form = FormServicio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Servicios')
    else:
        form = FormServicio()
            
    context = {
        'form' : form
    }     
    return render(request, 'servicios/nuevo_servicio.html', context)

@login_required
def eliminar_orden(request, id_orden):
    orden = OrdenServicio.objects.get(id_orden = id_orden)
    orden.delete()
    return redirect('Servicios')

@login_required
def eliminar_equipo(request, serial_number):
    equipo = Equipo.objects.get(serial_number = serial_number)
    equipo.delete()
    return redirect('Equipos')

@login_required
def editar_orden(request, id_orden):
    orden = OrdenServicio.objects.get(id_orden = id_orden)
    form = FormEditarOrden(instance=orden)

    if request.method == 'POST':
        form = FormEditarOrden(request.POST,  instance=orden)
        if form.is_valid():
            form.save()
            return redirect('Servicios')
            
    context = {
        'form' : form
    }
    return render(request, 'servicios/editar_orden.html', context)

@login_required
def editar_equipo(request, serial_number):
    equipo = Equipo.objects.get(serial_number = serial_number)
    form = FormEditarEquipo(instance=equipo)

    if request.method == 'POST':
        form = FormEditarEquipo(request.POST,  instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('Equipos')
            
    context = {
        'form' : form
    }
    return render(request, 'equipos/editar_equipo.html', context)

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    
    for usuario in usuarios:
        grupo = usuario.groups.all()

    context={
        'usuarios' : usuarios,
        'grupos' : grupos
    }
    return render(request, 'usuarios/lista_usuarios.html',context)

@login_required
def asignar_grupo(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        grupo = request.POST.get('grupo')
        grupo_actual = usuario.groups.first()
        usuario.groups.remove(grupo_actual)
        usuario.groups.add(grupo)
        usuario.save()
        return redirect('usuarios')
    grupos = Group.objects.all()
    context={
        'grupos' : grupos
    }
    return render(request, 'usuarios/asignar_permiso.html',context)


@login_required
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')
