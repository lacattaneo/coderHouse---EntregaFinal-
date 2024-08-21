from django.urls import path
from AppFinal.views import index,aboutCorrientes,exploraCorrientes

urlpatterns = [
    path('', index, name='index'),
    path('aboutCorrientes/', aboutCorrientes, name='aboutCorrientes'),
    path('exploraCorrientes/', exploraCorrientes, name='exploraCorrientes')
    
]