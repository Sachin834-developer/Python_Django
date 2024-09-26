"""
Inheritance : it is an ability in OOP that we can make use of methods and 
attributes of another class (conventionally refer to base class or parent
class ) in child class.

 it very useful that we can make use of the methods in the parent class and can overide the same method in the child class 
 without effecting the parent class method.

 if we want to extends the base class in different way that where 
 it is more useful , then for thr methods in the  base class, 
 we can add more functionality to them in child classes 

Types of Inheritance in python
1. Single
2. Multiple
3. Multi-level
4. Diamond 
"""


class Employee:
    hike_percent = 0.6

    def __init__(self, fname, lname, age, salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary

    def gen_email(self):
        print("parent class method")
        return self.fname + self.lname + "@gmail.com"

    def __str__(self):
        return f"{self.fname}"

    @classmethod
    def change_amount(cls, amount):
        hike_percent = amount

    def apply_hike(
        self,
    ):  # we can use by classname.varibalename  # Employee.hike_percent
        return self.salary + (
            self.hike_percent * self.salary
        )  # here we are refering class variable with instance


# emp_1= Employee('sachin','km',25,25000)
# emp_2= Employee('guru','yadki',25,30000)


class Developer(Employee):

    def __init__(self, fname, lname, age, salary, prog_lang):
        super().__init__(fname, lname, age, salary)
        self.prog_lang = prog_lang  # when we create object for the developer class , Emloyee classes __init__ method
        # is going handle the initialisaton for fname,lname,age,salary
        # Employee.__int__(self,fname,lname,age,salary)  we will use like this for multiple inheritance

    def gen_email(self):
        print("Child class method")
        super().gen_email()  # here we're calling parent class method inside the child class


dev_1 = Developer("sachin", "km", 25, 25000, "python")
# dev_1.hike_percent=1.1
dev_2 = Developer("guru", "yadki", 25, 30000, "java")
""" 
print(dev_1.fname)
print(dev_1.prog_lang)
print(isinstance(dev_1,Developer))  # calling instance method on class  
print(issubclass(Developer,Employee))
"""
print(help(Developer))  # To know the heirarchy on which order it going to execute


# print(dev_1.gen_email())
# print(Employee.gen_email(dev_1))
# print(Developer.gen_email(dev_1))




# ****************************************************************************************************
# Diamond Inheritance Example
# Let's break it down with an example:

# Base Class
class A:
    def __init__(self):
        print("Class A initialized")
        
# Intermediate Classes
class B(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__
        print("Class B initialized")
        
class C(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__
        print("Class C initialized")

# Derived Class that inherits from both B and C
class D(B, C):
    def __init__(self):
        super().__init__()  # Calls B and C's __init__
        print("Class D initialized")

# Create an instance of D
d = D()
# Output:

# Class A initialized
# Class C initialized
# Class B initialized
# Class D initialized
"""
Explanation:
Class A is the base class.
Class B and Class C both inherit from Class A.
Class D inherits from both Class B and Class C, creating a diamond-shaped hierarchy.
Method Resolution Order (MRO):
When you create an instance of D and call super(), Python follows the MRO to determine which class's __init__() method should be called next. You can inspect the MRO of the class D using:

"""
print(D.__mro__)
# The output will be:
"""
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
This tells Python to call the __init__() methods in the following order:

D.__init__()
B.__init__()
C.__init__()
A.__init__()

How super() Works in Diamond Inheritance:
When super() is called in D.__init__(), it invokes B.__init__().
In B.__init__(), super() is called again, which follows the MRO and invokes C.__init__().
In C.__init__(), super() is called, which then invokes A.__init__().
This ensures that each class in the hierarchy is initialized exactly once, avoiding multiple calls to A.__init__() that could happen if you manually called each parent class's __init__() method.

Summary:
Python’s super() handles diamond inheritance correctly by following the MRO, ensuring that each class in the inheritance chain is called only once.
The MRO resolves the order in which methods should be invoked, which prevents repeated calls to the common base class and handles complex inheritance patterns efficiently.
"""





