from django.db import models
from user.models import User
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    def is_available_for_issue(self):
       return not IssuedBook.objects.filter(book=self).exists() and not ReservedBook.objects.filter(book=self).exists()

class IssuedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'

class ReservedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
    
    def save(self, *args, **kwargs):
        if self.is_returned and not self.returned_date:
            self.returned_date = timezone.now().date()
        super().save(*args, **kwargs)

class ReturnedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    returned_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'



