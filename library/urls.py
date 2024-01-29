from django.urls import path
from .views import AuthorView, BookView, IssuedBookView, ReservedBookView, ReturnedBookView

urlpatterns = [
    path('author/', AuthorView.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
    path('author/<int:pk>/', AuthorView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='author-detail'),

    path('book/', BookView.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
    path('book/<int:pk>/', BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='book-detail'),

    path('issuedbook/', IssuedBookView.as_view({'get': 'list', 'post': 'create'}), name='issuedbook-list'),
    path('issuedbook/<int:pk>/', IssuedBookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='issuedbook-detail'),

    path('reservedbook/', ReservedBookView.as_view({'get': 'list', 'post': 'create'}), name='reservedbook-list'),
    path('reservedbook/<int:pk>/', ReservedBookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reservedbook-detail'),

    path('returnedbook/', ReturnedBookView.as_view({'get': 'list', 'post': 'create'}), name='returnedbook-list'),
    path('returnedbook/<int:pk>/', ReturnedBookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='returnedbook-detail'),
    
   
]
