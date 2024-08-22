from django.shortcuts import render

# Create your views here.

def listadoProductos(request):

    list_productos = [
        {'nombre': 'Producto 1', 'precio': 1000},
        {'nombre': 'Producto 2', 'precio': 2000},
        {'nombre': 'Producto 3', 'precio': 3000},
        {'nombre': 'Producto 4', 'precio': 4000}
    ]

    context = {
        'list_productos': list_productos
    }
    
    return render(request, 'myApp/producto.html', context)