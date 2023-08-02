from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="Home"),
    path('signup/', views.SignUp, name="SignUp"),
    path('productos/', views.Products, name="Productos"),
    path('clientes/', views.Clientes, name="Clientes"),
    path('productos/create', views.createProduct, name='createProducto'),
    path('productos/<int:productoId>/', views.detalleProducto, name='detalleProducto'),
    path('logout/', views.SignOut, name="LogOut"),
    path('logIn/', views.LogIn, name="LogIn")
]
