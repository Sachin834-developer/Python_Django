"""

Instance /Regular methods:  Regular methods automatically expect instance as the first argument.
when you try to access with the instance it automatically passes that instance as a first
parameter to the method.

Class Methods: As by default all methods expect class instance as a first param ,
class methods use @classmethod decorator make 
it to  expect class as a first parameter .
useful when we want to change the class variables 

by convention we use 'cls' as first param in the method to represent the class .

Static Methods:  As Instance and class methods ., static methods does not pass expect any
parameter automatically they are more similer 
like the functions except we're using them inside the class as they 
somehow how has some logical connections with the class .

  these are represent as a better use case when we don't use instance or class inside the method . 

  ex: date and days and months , to check is it a weekday or not , check some logic and return the result .


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

    @classmethod
    def change_amount(cls, amount):
        print("call")
        Employee.hike_percent = amount

    def apply_hike(
        self,
    ):  # we can use by classname.varibalename  # Employee.hike_percent
        return self.salary + (
            self.hike_percent * self.salary
        )  # here we are refering class variable with instance


emp_1 = Employee("sachin", "km", 25, 25000)
emp_2 = Employee("guru", "yadki", 25, 30000)

print(dir(emp_1))
emp_1.change_amount(0.9)
print(emp_1.hike_percent)
print(dir(emp_1))
print(emp_1.apply_hike())
