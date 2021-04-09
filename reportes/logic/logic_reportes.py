from ..models import reportes

def get_reportes():
    queryset = Reportes.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_reportes(form):
    reportes = form.save()
    reportes.save()
    return ()