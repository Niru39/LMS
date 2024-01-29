from rest_framework import permissions

class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'Student'

class IsLibrarianUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'Librarian'
    
class IsTeacherUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'Teacher'
