from django.urls import path
from . import views
app_name = 'Skincare'
urlpatterns = [
    path('Skin', views.Skin, name='Skin'),
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('shop', views.shop, name='shop'),
    path('body', views.body, name='body'),
    path('services', views.services, name='services')
]