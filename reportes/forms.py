from django import forms
from .models import Reportes

class ReportesForm(forms.ModelForm):
    class Meta:
        model = reportes
        fields = [
            'variable',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }
