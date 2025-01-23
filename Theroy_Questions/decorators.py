"""
2. Describe decorators and their use cases. Provide an example of creating a custom decorator 
    and explain its purpose with an example?

   Decorators in Python are a powerful feature that allows you to modify or extend the behavior 
   of functions or methods without changing their actual code. They are denoted by the @decorator_name 
   syntax and are primarily used for code reusability, logging, authorization, caching, 
   and other cross-cutting concerns in a clean and concise manner.
					OR
   Decorators in Python are functions that modify the behavior of other functions or methods.
 
   They are widely used in Python for enhancing the functionality of functions without modifying 
   their code directly.

   Decorators provide a clean and reusable way to add additional features to 
   functions, making the code more modular and maintainable.

	Use cases of decorators include:

	-- Logging: Adding logging statements to track function calls and their outputs.

	-- Caching: Storing the results of expensive function calls to avoid recomputatnio.

	-- Authentication: Checking user authentication before executing certain functions.

	-- Timing: Measuring the execution time of functions.

	-- Validation: Checking the input parameters of functions before execution.

	-- Error handling: Catching and handling exceptions raised by functions.

    Decorators are define from the 2 concepts that are functions are objects (first class fns)  and
      functions can be passed as parameters to other functions.

    Functions are objects and that can be assigned to other variables and treat them as functions

def hello():
    print('hello')

greet = hello

print(greet)
del hello

greet()



 Idea of returning a function with in another function

def hello(name):
    print('hello function executed')

    def welcome():
        print('\t I am welcome function inside hello')

    return welcome # here we are returning the function welcome not executing this ,
    so this can be executed out of the hello function.

greet=hello('sachin')
print(greet) #<function hello.<locals>.welcome at 0x0000017C6CACB940>

print(greet()) #I am welcome function inside hello


Function takes function as a a parameter and function inside a function.
 Passing some other function and executing a function inside the another function.

def hii():
    print("i am hii")

def hello(func):
    print('executing other func')
    print(func())

greet=hello(hii) # paassing function as param and executing inside the function.

    
#Let's create decorator

def new_decorator(func):

    def wrapper(*args,**kwargs):
        print(' before decoration ')
        result = func()
        print(' after decoration ')

    return wrapper

@new_decorator 
def need_decoration():
    print('I am decorated')


# Instead of calling a decorator like this , python makes it simpler by keeping a call above the function with @decorator name 
decorated_func=new_decorator(need_decoration)
print(decorated_func) #<function new_decorator.<locals>.wrapper at 0x0000025CEE6AB9D0>
print(decorated_func())

need_decoration() 

 example 
 """


def decorater_func(func):
    def wrapper_func(*args, **kwargs):
        print(
            *args
        )  # here it accepts the params that are passed to the original function .
        result = func(*args, **kwargs)
        print(result)  # after executong original function
        # if result.islower():
        return result.upper()

    return wrapper_func


@decorater_func
def display(name):
    return name


res = display("sachin")
print(res)


"""
def hii():
    return f'I am Hii'
    
def hello(func):
    def wrapper():
        print('I am inside Hello')
        return func()
    return wrapper
    
greet= hello(hii)
print(greet)
print(greet())
"""


def validate_params(func):
    def wrapper_func(*args, **kwargs):
        # Validate positional arguments
        valid_args = all(isinstance(arg, int) for arg in args)

        # Validate keyword arguments (if any)
        valid_kwargs = all(isinstance(value, int) for value in kwargs.values())

        if valid_args and valid_kwargs:
            return func(*args, **kwargs)
        else:
            return "Invalid Input"

    return wrapper_func


@validate_params
def add(a, b):
    return f"Sum of {a} and {b} is {a + b}"


@validate_params
def mul(a, b):
    return a * b


# Test cases
print(add(3, 4))  # Valid input
print(add(3, "4"))  # Invalid input
print(mul(5, 6))  # Valid input
print(mul(5, 6, c=2))  # Keyword arguments are not validated, but valid
print(mul(5, "6"))  # Invalid input
