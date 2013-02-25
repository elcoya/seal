from seal.model.course import Course
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from seal.model.teacher import Teacher
from seal.model.student import Student
from seal.model.delivery import Delivery
from seal.model.correction import Correction

@login_required
def index(request):
    courses = Course.objects.all()
    table_contents = []
    for course in courses:
        table_contents.append({'pk': course.pk, 'name': course.name, 'count': course.get_student_count()})
    table_deliveries = []
    teacher = Teacher.objects.get(user=request.user) 
    students = Student.objects.filter(corrector=teacher)
    for student in students:
        deliveries = Delivery.objects.filter(student=student)
        for delivery in deliveries:
            correction = Correction.objects.filter(delivery=delivery)
            table_deliveries.append({'pk': delivery.pk, 'delierydate': delivery.deliverDate, 'student': delivery.student, 'practice': delivery.practice, 'correction':correction})
    return render_to_response('teacher/index.html', {'table_contents': table_contents, 'deliveries': table_deliveries}, context_instance=RequestContext(request))
