from django.urls import path
from .views import listadoProductos

urlpatterns = [
    path('listadoProductos/', listadoProductos, name='listadoProductos'),
]
