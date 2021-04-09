from django.urls import path

from . import views

urlpatterns = [
    path('actividades/',views.actividades_create),
    path('actividadesCreate/', views.actividades_create, name='actividadesCreate'),
]