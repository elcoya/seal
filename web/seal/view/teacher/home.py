from seal.model.course import Course
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    courses = Course.objects.all()
    table_contents = []
    for course in courses:
        table_contents.append({'pk': course.pk, 'name': course.name, 'count': course.get_student_count()})
    return render_to_response('teacher/index.html', {'table_contents': table_contents}, context_instance=RequestContext(request))
