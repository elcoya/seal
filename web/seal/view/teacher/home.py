from seal.model.course import Course
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from seal.model.teacher import Teacher
from seal.model.student import Student
from seal.model.delivery import Delivery
from seal.model.correction import Correction
from seal.settings import HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def index(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
                status = delivery.get_automatic_correction().get_status()
                if (status == "successfull"):
                    table_deliveries.append({'delivery': delivery, 'correction':correction})
        return render_to_response('teacher/index.html', {'table_contents': table_contents, 'table_deliveries': table_deliveries}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
