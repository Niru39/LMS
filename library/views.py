from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, IssuedBook, ReservedBook, ReturnedBook
from .serializers import AuthorSerializer, BookSerializer, IssuedBookSerializer, ReservedBookSerializer, ReturnedBookSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CanIssueBook, CanReserveBook, CanReturnBook, CanViewBook, CanPostBook
from django.db import models
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from  django_filters.rest_framework import DjangoFilterBackend
from user.permissions import IsLibrarianUser

class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    def get_permissions(self):
        if self.action in ['create', 'update']:
            return [IsLibrarianUser()]
        else:
            return [IsAuthenticated()] 

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [CanViewBook]  
    filter_backends = [SearchFilter]
    search_fields = ['title','author_name']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [CanPostBook()]
        else:
            return [CanViewBook()]
        
    def list(self, request, *args, **kwargs):
        
        search_query = self.request.query_params.get('search', None)

        if search_query:
            # to filter books by title or author name
            
            filtered_books = self.queryset.filter(
                models.Q(title__icontains=search_query) | models.Q(author__name__icontains=search_query)
            )
            
            #  to check availability for each book
            available_books = []
            for book in filtered_books:
                if book.is_available_for_issue():
                    available_books.append(book)

            serializer = self.get_serializer(available_books, many=True)
            print(f"Serialized Data: {serializer.data}")
            return Response(serializer.data)
        else:
            # If no search query provided, return all books
            response = super().list(request, *args, **kwargs)
            print(f"Response Data: {response.data}")
            return response

    
    

class IssuedBookView(ModelViewSet):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer
    permission_classes = [CanIssueBook]
 

class ReservedBookView(ModelViewSet):
    queryset = ReservedBook.objects.all()
    serializer_class = ReservedBookSerializer
    permission_classes = [CanReserveBook]
    

class ReturnedBookView(ModelViewSet):
    queryset = ReturnedBook.objects.all()
    serializer_class = ReturnedBookSerializer
    permission_classes = [CanReturnBook]
    
    
