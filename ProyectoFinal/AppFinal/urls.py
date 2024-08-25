from django.urls import path
from AppFinal.views import index,chamame,ibera, pesca, padre, carnaval,yo

urlpatterns = [
    path('', index, name='index'),
    path('chamame/', chamame, name='chamame'),
    path('ibera/', ibera, name='ibera'),
    path('pesca/',pesca,name='pesca'),
    path('padre/', padre, name="padre"),
    path('carnaval/', carnaval, name="carnaval"),
    path('yo/', yo, name="yo")
]