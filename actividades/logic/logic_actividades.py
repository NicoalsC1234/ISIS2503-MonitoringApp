from ..models import Actividades

def get_actividades():
    queryset = Actividades.objects.all()
    return (queryset)

def create_actividades(form):
    actividades = form.save()
    actividades.save()
    return ()