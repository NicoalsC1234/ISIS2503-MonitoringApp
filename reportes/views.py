from django.shortcuts import render
from .forms import ReportesForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_reportes import create_reportes, get_reportes

def reportes_list(request):
    reportes = get_reportes()
    context = {
        'reportes_list': reportes
    }
    return render(request, 'Reportes/reportes.html', context)

def reportes_create(request):
    if request.method == 'POST':
        form = ReportesForm(request.POST)
        if form.is_valid():
            create_reportes(form)
            messages.add_message(request, messages.SUCCESS, 'Reportes create successful')
            return HttpResponseRedirect(reverse('ReportesCreate'))
        else:
            print(form.errors)
    else:
        form = ReportesForm()

    context = {
        'form': form,
    }

    return render(request, 'Reportes/reportes Create.html', context)