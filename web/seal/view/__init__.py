#expected http responses#######################################################
from django.http import HttpResponse
HTTP_401_UNAUTHORIZED_RESPONSE = HttpResponse('You are not authorized here.', 401)
###############################################################################

