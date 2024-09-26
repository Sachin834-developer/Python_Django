"""
What are generators in python and give me a real world example?

In Python, generators are a type of iterable, similar to lists or tuples,
but they allow you to generate 
values on-the-fly rather than storing them in memory. 
Generators are implemented using functions and the yield keyword.
When a generator function is called, it returns a generator object, 
which can be iterated over using a loop or other iteration methods.

The key benefit of generators is that they are memory-efficient since they don't store 
the entire sequence of values in memory at once. 
Instead, they produce each value one by one when requested, which is particularly 
useful when dealing with large datasets or 
infinite sequences.

-----------OR--------------
A generator function in Python is defined like a normal function, but whenever it needs to 
generate a value, 
it does so with the yield keyword rather than return. If the body of a def contains yield, 
the function automatically becomes a Python generator function.

# Insted of return, generator function uses yield keyword .

Generator Object:
Python Generator functions return a generator object that is iterable, i.e., can be used as
an Iterator.
 Generator objects are used either by calling the next method of the generator object 
 or using the generator object in a “for in” loop.
"""

# Fibanocci function
# 0,1,1,2,3,5,8,13,21

# n= (n-1)+(n-2)
"""
# without using Geneartor .
def fibanocci(n):

    a=0
    b=1
    fib_list=[]
    while n>0:
        fib_list.append(a) #0, 1,2,
        a, b = b, a + b
        n-=1
    return fib_list
print(fibanocci(5))
"""


# using Geneartor
def fibanocci(n):

    a, b = 0, 1

    for _ in range(n):
        yield a  # 0 , 1 , 2
        # a=b
        # b=a+b # 1 , 2   ... this will throw the wrong output
        a, b = b, a + b  # 1,1 ,, 1,
        # 1 , # 2


"""
def my_gen(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
            
for i in my_gen(10):
    print(i)
    
print(fibanocci(10)) #<generator object fibanocci at 0x000002064F764C10>

print(gen_object)  #<generator object fibanocci at 0x000002064F764C10>  
# geneartor functions always returns the genrator objects 
"""
# we can use the next() func on the generator objects to get the value
gen_object = fibanocci(5)
"""
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))  # if the genrator object is emptied then it throws the StopIteration error .

# to avoid this use for loops  on the generator objects

for num in gen_object:
    print(num)
"""
# Genrator comprehension
gen_list = (num for num in fibanocci(5))

for num in gen_list:
    print(num)


# Iterators and iterables
# iter() function , next() function

my_list = [10, 20, 30, 40]

it_object = iter(my_list)
print(next(it_object))
print(next(it_object))
print(next(it_object))
print(next(it_object))

for num in it_object:
    print(num)
