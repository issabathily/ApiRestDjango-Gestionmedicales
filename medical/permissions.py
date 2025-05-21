from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

User = get_user_model()

class IsMedicalStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.profile.role in ['doctor', 'nurse']
        except AttributeError:
            return False

class IsPatientDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return obj.doctor == request.user
        except AttributeError:
            return False

class HasMedicalRecordAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            if request.user.profile.role == 'doctor':
                return obj.doctor == request.user
            elif request.user.profile.role == 'nurse':
                return True
            elif request.user.profile.role == 'admin':
                return True
            return False
        except AttributeError:
            return False
