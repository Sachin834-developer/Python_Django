"""
In Django, relationships between models (database tables) are established using fields that represent various types of relationships. These include OneToOne, ForeignKey (One-to-Many), and ManyToMany relationships. Each of these relationships corresponds to a different type of association between models, and Django provides fields to handle these associations.

1. One-to-One Relationship (OneToOneField)
A One-to-One relationship means that for every instance of a model, there is exactly one related instance in another model. In terms of databases, this is equivalent to a unique foreign key relationship. For example, a Profile model may have a one-to-one relationship with a User model, meaning that each user has exactly one profile, and each profile is associated with exactly one user.

Usage: In this example, the Profile model has a OneToOneField to the User model, meaning that each user can have only one profile.
on_delete=models.CASCADE: This means that if the related User instance is deleted, the corresponding Profile instance will also be deleted.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)


"""
2. One-to-Many Relationship (ForeignKey)
A One-to-Many relationship is established using a ForeignKey. This means that one instance of a model can be related to many instances of another model. For example, a Book model can have a foreign key to an Author model, meaning that one author can write many books, but each book is written by only one author.

Usage: In this example, the Book model has a ForeignKey to the Author model, indicating that a book is associated with a single author, but an author can write multiple books.
on_delete=models.CASCADE: If the related Author instance is deleted, all associated Book instances will also be deleted.
"""


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


"""
3. Many-to-Many Relationship (ManyToManyField)
A Many-to-Many relationship means that each instance of a model can be related to multiple instances of another model, and vice versa. This relationship requires a join table in the database to manage the connections. For example, a Student model can have a many-to-many relationship with a Course model, meaning that a student can enroll in multiple courses, and a course can have multiple students enrolled.

Usage: In this example, the Student model has a ManyToManyField to the Course model, meaning that a student can enroll in multiple courses, and a course can have multiple students.
Behind the scenes: Django automatically creates an intermediary table to manage this many-to-many relationship. You can also define a custom intermediary model if you need to store additional information in the relationship.

NOTE: 1. Django creates a New DB table handle many to many relationships
    2. on_delete  can have CASCADE, PROTECT , SET_NULL, SET_DEFAULT
    
"""


class Course(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, on_delete=models.SET_NULL)
