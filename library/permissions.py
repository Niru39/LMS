# permissions.py
from rest_framework.permissions import BasePermission

class CanViewBook(BasePermission):
    def has_permission(self, request, view):
        
        return True

class CanPostBook(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.user_type == 'Librarian'

class CanViewBook(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.user_type in ['Student', 'Teacher','Librarian']

class CanIssueBook(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.user_type in ['Student', 'Teacher']

class CanReturnBook(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.user_type in ['Student', 'Teacher']

class CanReserveBook(BasePermission):
    def has_permission(self, request, view):
        
        return request.user.user_type in ['Student', 'Teacher']

