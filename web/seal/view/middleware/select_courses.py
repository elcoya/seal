"""

@author: anibal

"""
from seal.model.course import Course

class CourseSelectionMiddleware:
    
    def process_response(self, request, response):
        response.courses = Course.objects.all()
        return response