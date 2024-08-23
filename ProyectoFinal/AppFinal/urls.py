from django.urls import path
from AppFinal.views import index,about,post, contact, padre

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/', post  , name='post'),
    path('contact/', contact,name='contact'),
    path('padre/', padre, name="padre")
    
]