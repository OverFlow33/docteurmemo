from rest_framework.permissions import BasePermission

class CanPredict(BasePermission):

    def has_permission(self, request, view):
        return request.user.doctor and request.user.doctor.field in  ('GNR',  'NRL')