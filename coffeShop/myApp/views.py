from django.shortcuts import render

# Create your views here.

def listadoProductos(request):
    
    return render(request, 'myApp/producto.html')