
from django.urls import path
from .views import home,servicio,formulario,listar_persona,eliminar_persona,modificar_persona



urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('servicio/', servicio, name="servicio"),
    path('formulario/', formulario, name="formulario"),
    path('listar-personas/', listar_persona, name="listado_personas"),
    path('eliminar-persona/<id>/', eliminar_persona, name="eliminar_persona"),
    path('modificar-persona/<id>', modificar_persona, name="modificar_persona"),
    
]