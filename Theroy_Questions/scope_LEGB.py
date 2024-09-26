"""
Python follows the LEGB rule to determine the scope of a variable, which stands for Local, Enclosing, 
Global, and Built-in.

Local Scope: Inside functions.
Enclosing Scope: For nested functions.
Global Scope: At the top level of the script or module.
Built-in Scope: Predefined functions and objects provided by Python.
"""

# 1. LOCAL SCOPE : Inside functions.

def local_scope():
    x = 20 
    print(x) # only accessble inside the fn

# print(x) # NameError: name 'x' is not defined
# local_scope()

# 2. ENCLOSING SCOPE : For nested functions.

def outer_func():
    x =10 # Enclosing scope
    def inner_func():
        nonlocal x # to modify enclosing scope var x inside local scope
        x=20
        print(x)
    inner_func()
    print(x) # modified enclosing var x 

# outer_func()


# 3. Global Scope: At the top level of the script or module

# x=10  #Global var
#  can be accessed from anywhere in the code, including inside functions (unless shadowed by a local variable with the same name).
def outer_func():
    # print(x)
    global x #global keyword to modify a global variable inside a function
    x =20
    def inner_func():
        print(x)
    inner_func()

# outer_func()
# print(x) # global var modified inside the func by making it local


# 4. Built-in Scope: Predefined functions and objects provided by Python.
# print(dir(__builtins__))
print(type())