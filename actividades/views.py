
import os

from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_actividades import create_actividades, get_actividades

def actividades_list(request):
    actividades = get_actividades()
    context = {
        'actividades_list': actividades
    }
    return render(request, 'Actividades/actividades.html', context)

def actividades_create(request):
    response = HttpResponse(content_type= 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Sprint2-student-assignments.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize =A4)


    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750,"08/04/2021")
    c.line(460,747,560,747)

    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    numero = Paragraph('''No.''',styleBH)
    alumno = Paragraph('''Alumno''',styleBH)
    b1 = Paragraph('''Actividad1''',styleBH)
    data = [[numero,alumno,b1]]

    alumnos = [{'#':'1','nombre':'Nicolas Chalee Guerrero', 'b1':'Leer 10 paginas del libro'}]

    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7

    width, height = A4
    high = 650
    for student in alumnos:
        this_student = [student['#'],student['nombre'],student['b1']]
        data.append(this_student)
        high = high -18

    table = Table(data, colWidths=[1.9*inch, 9.5*inch,1.9*inch,1.9*inch,1.9*inch,1.9*inch])
    table.setStyle(TableStyle([('INNERGRID',(0,0),(-1,-1),0.25, colors.black),('BOX',(0,0),(-1,-1),0.25, colors.black),]))

    table.wrapOn(c,width,height)
    table.drawOn(c,30,high)
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
    return render(request, 'Actividades/actividadesCreate.html', context)
