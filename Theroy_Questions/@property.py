"""
@property decorator allow us to access the methods inside the class as 
variables , along with using methods 
like setter and deleter we can do those 
opertaions to that method

getter  --> @property

setter --> 

deleter --> 

 *** Getter and Setter Methods in Python ***
 
Getter and Setter methods are used to access and modify the private attributes of a class. These methods provide an interface for interacting with private or protected data, without giving direct access to that data. This ensures that any changes to the internal state of the object are controlled, which is a key aspect of encapsulation.

"""
class Student:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    @property
    def fullname(self):
        return self.fname+' '+self.lname
    
    @property
    def gmail(self):
        return f'{self.fname}.{self.lname}@gmail.com'
    
    @fullname.setter
    def fullname(self,value):
        self.fname,self.lname=value.split()

    @fullname.deleter
    def fullname(self):
        self.fname=self.lname=None

student_1=Student('sachin','km',25)
print(student_1.fullname)
student_1.fullname= 'guru yadki'  # setter method called in the class treat like varibale and set the value
print(student_1.fullname)
print(student_1.gmail)
# del student_1.fullname  # deleter method associtaed with the method gets called and do the operations of setting values to None 
# print(student_1.fname)


# EXAMPLE 2
# Pythonic Approach: Property Decorators
# In Python, you can also use @property decorators to create getters and setters in a more concise way. This is a more Pythonic approach and makes the code look cleaner.

# This approach allows you to use getters and setters more seamlessly without explicitly calling methods like get_name() or set_name().

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name")
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age")

# Usage
person = Person("Alice", 25)
print(person.name)  # Calls the getter
person.age = 30     # Calls the setter
print(person.age)   # Calls the getter
