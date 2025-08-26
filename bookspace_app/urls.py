from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/', views.empresa, name='empresa'),
    path('productos/', views.productos, name='productos'),
    path('oferta-del-mes/', views.oferta_del_mes, name='oferta_mes'),
    path('localizacion/', views.localizacion, name='localizacion'),
    path('contacto/', views.contacto, name='contacto'),
    path('noticias/', views.noticias, name='noticias'),
    path('clima/', views.clima, name='clima'),
    path('login/', views.login_view, name='login'),
    path('obtener-clima/', views.obtener_clima, name='obtener_clima'),
]

