from django.shortcuts import render, redirect
from .models import DatosPersona
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def servicio(request):
    return render(request, 'core/servicio.html')

def formulario(request):

    persona = DatosPersona.objects.all()
    variables = {
        'persona':persona
    }

    if request.POST:
        persona = DatosPersona()
        persona.Nombre = request.POST.get('txtNombre')
        persona.Direccion = request.POST.get('txtDireccion')
        persona.Telefono = request.POST.get('txtTelefono')
        persona.Mail = request.POST.get('emailMail')
        persona.Asunto = request.POST.get('txtasunto')
        persona.Mensaje = request.POST.get('txtmensaje')

        try:
            persona.save()
            variables['mensaje'] = 'Guardado Exitoso'
            mensaje = "Guardado Exitoso"
            messages.success(request, mensaje)

        except:
            variables['mensaje'] = 'Error No se a podido Guardar'
            mensaje = "Error No se a podido Guardar"
            messages.success(request, mensaje)



    return render(request, 'core/formulario.html', variables)

#CRUD

def listar_persona(request):

    personas = DatosPersona.objects.all()

    return render(request, 'core/listar_persona.html', {'personas':personas})

def eliminar_persona(request, id):
    #primero hay que buscar
    persona = DatosPersona.objects.get(id=id)

    try:
        persona.delete()
        mensaje = "Datos de la Persona Eliminados"
        messages.success(request, mensaje)
    except:
        mensaje = "No se han Podido Eliminar los Datos"
        messages.error(request, mensaje)
    return redirect('listado_personas')

def modificar_persona(request, id):
    persona = DatosPersona.objects.get(id=id)

    variables = {
        'persona':persona
    }

    if request.POST:
        persona = DatosPersona()
        persona.id = request.POST.get('txtId')
        persona.Nombre = request.POST.get('txtNombre')
        persona.Direccion = request.POST.get('txtDireccion')
        persona.Telefono = request.POST.get('txtTelefono')
        persona.Mail = request.POST.get('emailMail')
        persona.Asunto = request.POST.get('txtasunto')
        persona.Mensaje = request.POST.get('txtmensaje')

        try:
            persona.save()
            variables['mensaje'] = 'modificado Exitoso'

        except:
            variables['mensaje'] = 'Error No se a podido modificar'

    return render(request, 'core/modificar_persona.html', variables)
    
