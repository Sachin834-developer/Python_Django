"""
__len__:

__str__: it meant be more of a readable representation of a object, used as a display to
the end user.

__repr__:  repr()  it is an unambigious representation of the object it is used to debugging
,logging , and other purposes ,
 it really meant to be used for the other developers


if we don't define __str__ on an class and if we call str on object its going to 
fallback on the repr method.


"""


class Employee:
    hike_percent = 0.6

    def __init__(self, fname, lname, age, salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary

    def gen_email(self):
        return self.fname + self.lname + "@gmail.com"

    def __repr__(self) -> str:
        return f"Employee({self.fname},{self.lname},{self.age},{self.salary})"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.fname) + len(self.lname)


emp_1 = Employee("sachin", "km", 25, 25000)
emp_2 = Employee("guru", "yadki", 25, 30000)
"""
print(repr(emp_1))  # it as similer as calling print(emp_1.__repr__()) 
print(str(emp_1))   #


# lot of special methods for arthmatic


print(int.__add__(1,2))  # int __add__ method actually adds 
print(str.__add__('a','b'))  # string __add__ mrthod concatinates 


 # if we define __add__ method in the class , we can direct how this method works 
print(emp_1+emp_2)  #  here we added our 2 employee salary just by using '+' operator 
"""
# example is the by __len__ method to return the number of characters in their full name
print(len(emp_1))

# __new__ is typically overridden in cases where you need more control over the object creation process, 
# such as when implementing
# singleton patterns, metaclasses, or when subclassing immutable types like int or str

# Example: When to Override __new__
# Here’s an example of overriding __new__ to implement a singleton pattern, where only one instance of the class is created:

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

obj1 = Singleton(10)
obj2 = Singleton(20)

print(obj1 is obj2)  # True (Both obj1 and obj2 refer to the same instance)
print(obj1.value)    # 20 (Since obj2 modified the value)
# In this example, __new__ ensures that only one instance of the Singleton class is created, 
# and both obj1 and obj2 refer to the same instance.