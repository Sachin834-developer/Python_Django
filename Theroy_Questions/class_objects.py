"""
classes allow us to logically group our data and  functions in a way that 
easy to reuse and build upon if needed.

create a class Employee which will have attributes like name ,age, salary. 

__init__  : It is special method used as constructor in python for the intialisation of the 
    instance variables. this method gets executed when the instance of the class is created. always
    __init__ methos takes instance as a first parameter and by convention in python we call 
    it as self keyword.

self : self represents the instance of the class. By using the “self”  we can access the 
attributes and methods of the class in python. It binds the attributes with the given arguments.

 Instance varibales: Instance variables are unique to each instance .Attributes defined on the
 class and holding data about specific objects are instance variables.
 Instance variables are created when an object is instantiated, and are accessible to all the 
 constructors, methods, or blocks in the class.

 Class variables:class variables are those variables which shared among all instances of a 
 class. these are same for all the instances these becomes very useful when the value of the 
 variable is remains same to the all the instances.

 if we create the instance variables with same name as the class variables , what happens is 
 when we tried to  access it first it checks in the object scope the variable is present or 
 not then in te class scope.

"""

""" 
class Employee:

    def __init__(self,fname,lname,age,salary):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.salary=salary

    def gen_email(self):
        return self.fname+self.lname+'@gmail.com'
    
    def __str__(self):
        return f'{self.fname}'

emp_1= Employee('sachin','km',25,25000)
emp_2= Employee('guru','yadki',25,30000)

print(emp_1)  # <__main__.Employee object at 0x0000023585191FD0>  or output of the __str__ function
print(emp_1.fname)  # inside Employee.fname(emp_1)

print(emp_1.gen_email())  # behind the scenes print(Employee.gen_email(emp_1))   it has run like this 

print(emp_2.fname)
print(emp_2.gen_email())

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

    def __str__(self):
        return f"{self.fname}"

    def apply_hike(
        self,
    ):  # we can use by classname.variable name  # Employee.hike_percent
        return self.salary + (
            self.hike_percent * self.salary
        )  # here we are referring class variable with instance

    def myemail(self):
        return self.gen_email()


emp_1 = Employee("sachin", "km", 25, 25000)
emp_2 = Employee("guru", "yadki", 25, 30000)

print(emp_1.apply_hike())
print(emp_2.apply_hike())
print(emp_2.__dict__)
emp_2.hike_percent = (
    0.8  # here it creates the hike_percent variable in the object(emp_2) scope
)
print(emp_2.__dict__)
print(emp_1.__dict__)
print(emp_2.apply_hike())
print(emp_1.myemail())
# will create class variable hike_percent
