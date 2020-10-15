from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,formulario,MisionyVision,login,logout_v

urlpatterns = [
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('mision_y_vision/',MisionyVision,name='MYV'),
    path('login/',login,name='LOGIN'),
    path('logout_v',logout_v,name='LOGOUT'),
]