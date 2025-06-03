from rest_framework.permissions import BasePermission


class ManagerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("hre3123")
        if request.user.is_authenticated:
            if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
                return request.user.is_manager
            else:
                return False
        else:
            print("here")
            if request.method in ["GET"]:
                return True
            return False
