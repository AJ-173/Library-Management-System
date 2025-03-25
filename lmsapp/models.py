from django.db import models

# Create your models here.
from django.db import models

# role = True is admin else normal User
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.BooleanField(default=False)

    def __str__(self):
        return self.email

# class Admin(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.email

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title
