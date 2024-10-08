from django.urls import path
from AppFinal.views import index,chamame,ibera, pesca, padre, carnaval,yo,registroUsuario, loginUsuario,loginPagina, comprarEntrada,perfilUsuario,userLogout, confirmacionCompra,resumenCompras,perfilUsuario

urlpatterns = [
    path('', index, name='index'),
    path('chamame/', chamame, name='chamame'),
    path('ibera/', ibera, name='ibera'),
    path('pesca/',pesca,name='pesca'),
    path('padre/', padre, name="padre"),
    path('carnaval/', carnaval, name="carnaval"),
    path('yo/', yo, name="yo"),
    path('registroUsuario/', registroUsuario, name='registroUsuario'),
    path('loginUsuario/', loginUsuario, name='loginUsuario'),
    path('loginPagina/', loginPagina, name='loginPagina'),
    path('perfilUsuario/', perfilUsuario, name='perfilUsuario'),
    path('logout/', userLogout, name='logout'),
    path('comprarEntrada/', comprarEntrada, name='comprarEntrada'),
    path('confirmacionCompra/',confirmacionCompra, name='confirmacionCompra'),
    path('resumenCompras/', resumenCompras, name='resumenCompras'),
    path('perfil/', perfilUsuario, name='perfilUsuario'),
]
