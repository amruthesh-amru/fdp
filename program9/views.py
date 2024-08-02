import csv
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Student

def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name'])

    students = Student.objects.all().values_list('name')
    for student in students:
        writer.writerow(student)
    return response

def export_students_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    p = canvas.Canvas(response)

    students = Student.objects.all()
    y = 800
    for student in students:
        p.drawString(100, y, f"Student Name: {student.name}")
        y -= 40

    p.showPage()
    p.save()
    return response
# Create your views here.
