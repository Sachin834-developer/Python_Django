"""
In Django, model inheritance allows you to create a hierarchy of classes that can share fields and methods, while also allowing for different behaviors depending on the type of inheritance you choose. Django supports three types of model inheritance: abstract base classes, multi-table inheritance, and proxy models. Each type serves a different purpose and is used in different situations.

1. Abstract Base Classes
Abstract base classes are used when you want to define common fields and methods for other models to inherit but you don't want to create a table for the base class itself in the database. The abstract base class is only a blueprint for the child models.

"""
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Student(CommonInfo):
    student_id = models.CharField(max_length=10)

class Teacher(CommonInfo):
    employee_id = models.CharField(max_length=10)

"""
2. Multi-Table Inheritance
Multi-table inheritance is used when you want each model in the hierarchy to have its own database table. This means that each subclass will have its own table, and the base class will also have its own table. A foreign key is automatically created to link the subclass table to the base class table."""

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Student(Person):
    student_id = models.CharField(max_length=10)

class Teacher(Person):
    employee_id = models.CharField(max_length=10)

"""
3. Proxy Models
Proxy models are used when you want to change the behavior of an existing model (like changing the default ordering, adding methods, or modifying the model's behavior) without modifying the model's fields or creating a new database table. The proxy model uses the same database table as the original model."""

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class PersonProxy(Person):
    class Meta:
        proxy = True
        ordering = ['-age']

    def get_name_uppercase(self):
        return self.name.upper()

# Understanding these different types of model inheritance is important for designing an efficient and scalable database schema in Django, depending on the specific needs of your application.