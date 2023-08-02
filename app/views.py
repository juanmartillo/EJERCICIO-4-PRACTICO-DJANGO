from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import productForm
from .models import Producto, cliente

# Create your views here.
def Home(request):    
    return render(request, "home.html")


def SignUp(request):
    if(request.method == "GET"):
        return render(request, "signup.html", {
        'form': UserCreationForm
    })
    else:
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                cliente_obj = cliente(name=user)
                cliente_obj.save()
                return redirect('Productos')
            except IntegrityError:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'message': 'Username already Exist'
                })
        return render(request, "signup.html", {
                    'form': UserCreationForm,
                    'message': 'Las contraseñas no coinciden'
                })
    
def Products(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def Clientes(request):
    clientes = cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def SignOut(request):
    logout(request)
    return redirect('Home')

def LogIn(request):
    if(request.method == "GET"):
        return render(request, "LogIn.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, "LogIn.html", {
                'form': AuthenticationForm,
                'message': "Usuario ontraseña incorrecto"
            })
        else:
            login(request, user)
            return redirect('Productos')

def createProduct(request):
    if request.method == "GET":
        return render(request, 'createProduct.html',{
            'form': productForm
        })
    else:
        try:
            form = productForm(request.POST)
            newProduct = form.save(commit = False)
            newProduct.user = request.user
            newProduct.save()
            return redirect('Productos')
        except ValueError:
            return render(request, 'createProduct.html',{
                'form': productForm,
                'error': 'Verifique si los datos son correctos'
            })

def detalleProducto(request, productoId):
    if request.method == 'GET':
        productoDetail = get_object_or_404(Producto, pk=productoId)
        form = productForm(instance=productoDetail)
        return render(request, 'productoDetalle.html',{'producto': productoDetail, 'form': form})
    else:
        try:
            productoDetail = get_object_or_404(Producto, pk=productoId)
            form = productForm(request.POST, instance=productoDetail)
            form.save()
            return redirect('Producto')
        except:
            return render(request, 'productoDetalle.html', {'prodcuto': productoDetail, 'form': form, 'error': 'Error updating task.'})
