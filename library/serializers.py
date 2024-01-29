from rest_framework import serializers
from .models import Author, Book, IssuedBook, ReservedBook, ReturnedBook
from user.serializers import UserSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Book
        fields = '__all__'

class IssuedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedBook
        fields = '__all__'

class ReservedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedBook
        fields = '__all__'

class ReturnedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnedBook
        fields = '__all__'


