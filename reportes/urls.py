from django.urls import path
from django.views.decorators.csrf import csrf_e xempt

from . import views

urlpatterns = [
    path('reportes/',views.reportes_list),
    path('reportescreate/', csrf_exempt(views.reportes_create), name='reportesCreate'),
]