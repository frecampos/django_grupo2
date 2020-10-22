from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,formulario,MisionyVision,login,logout_v,insumos,admin_insumos,eliminar,buscar_insumo,modificar_insumo

urlpatterns = [
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('mision_y_vision/',MisionyVision,name='MYV'),
    path('login/',login,name='LOGIN'),
    path('logout_v',logout_v,name='LOGOUT'),
    path('insumos/',insumos,name='INSUMOS'),
    path('admin_insumos/',admin_insumos,name='ADMININSUMOS'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('buscar/<id>/',buscar_insumo,name='BUSCAR'),
    path('modificar/',modificar_insumo,name='MODIFICAR'),
]