"""

@author: anibal

"""
from rest_framework import permissions
from seal import settings
import rest_framework

class ApplicationKeyPermission(permissions.BasePermission):
    """
    Authorizes requests if they provide the expected key
    """
    
    application_key = settings.DAEMON_KEY
    admin_permission = rest_framework.permissions.IsAdminUser()
    
    def has_permission(self, request, view, obj=None):
        has_admin_permissions = self.admin_permission.has_permission(request, view)
        if has_admin_permissions:
            return has_admin_permissions
        
        try:
            key = request.META["HTTP_KEY"]
            return key == self.application_key
        except:
            return False
