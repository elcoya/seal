from seal.model.course import Course
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from seal.model.teacher import Teacher
from seal.model.student import Student
from seal.model.delivery import Delivery
from seal.model.correction import Correction
from seal.view.teacher import user_is_teacher


@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def index(request, idcourse=None):
    courses = Course.objects.all()
    if idcourse is None:
        try:
            current_course = courses.latest('pk')
        except:
            current_course = None
    else:
        current_course = courses.get(pk=idcourse)
    table_contents = []
    for course in courses:
        table_contents.append({'pk': course.pk, 'name': course.name, 'count': course.get_student_count()})
    table_deliveries = []
    teacher = Teacher.objects.get(user=request.user) 
    students = Student.objects.filter(corrector=teacher)
    for student in students:
        deliveries = Delivery.objects.filter(student=student, practice__course=current_course)
        for delivery in deliveries:
            correction = Correction.objects.filter(delivery=delivery)
            status = delivery.get_automatic_correction().get_status()
            if (status == "successfull"):
                table_deliveries.append({'delivery': delivery, 'correction':correction})
    return render_to_response('teacher/index.html', 
                              {'current_course' : current_course,
                               'courses' : courses,
                               'table_contents': table_contents, 
                               'table_deliveries': table_deliveries}, 
                              context_instance=RequestContext(request))
