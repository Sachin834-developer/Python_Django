"""
1. What is Exception handling in python  and why it is essential in python?

Exception handling in Python is a crucial concept that allows you to gracefully 
handle errors and prevent our program from crashing unexpectedly.

It's essential to use exception handling judiciously to ensure our program can 
handle potential errors gracefully and provide informative error messages when necessary.
Since web applications deal with user input and interactions, errors are common. 

Exception handling ensures that even if an error occurs, the application can display a 
helpful error message to users or log the error for debugging, rather than displaying a 
generic error page or causing the server to crash.

Handled using the try, except ,else,finally blocks of code.
"""


def samplefunc():
    pass


try:
    # code that may raise an exception
    result = samplefunc()
except ValueError as e:  # ValueError, syntaxError, AttributeError
    # code to handle the specific exception
    print("specific error occured")
except AttributeError as e:
    # code to handle the specific exception 2
    print("specific error 2 as occured")
else:
    # code that runs only when there is no exceptions
    print("No errors")
finally:
    # code that always runs regard less of an error occured or not
    print("this will always execute")

"""
try: The try block contains the code that might raise an exception. You place the code that 
is susceptible to errors inside this block.

except: The except block is used to catch and handle specific exceptions that 
may occur within the try block. If an exception occurs, 
Python will look for a matching except block that can handle that type of exception. 

	IMP: If no matching except block is found, the program will terminate with an error message.

finally: The finally block contains code that will always be executed, 
regardless of whether an exception was raised or not. 
It is typically used for cleanup actions, such as closing files or releasing resources.

else: The else block will execute only if no exception occurs in the try block. 
It is often used to perform additional actions when the try block succeeds without any exceptions.

"""

s = 1
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    raise Exception("Error: Cannot divide by zero")

# Example 2   , Handle Type error with invalid index
# Example 3   , Key error for dicts with invalid keys.

items = ["apple", "banana", "apple", "cherry", "banana", "banana"]

try:
    # print(items['fsv',])
    print(items[10])
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("No Error")
finally:
    print("Done")


# Attribute Error
# Missing Initialization: An attribute may not have been set during the object initialization.


class MyClass:
    def __init__(self):
        pass


obj = MyClass()
print(obj.attribute)  # Raises AttributeError because attribute is not defined
