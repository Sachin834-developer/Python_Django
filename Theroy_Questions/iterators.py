"""


"""

my_list=[1,2,3,4,5]
#Here the list is a iterable , so that it allow us to loop over 
# list object will return an iterator object from its __iter__() method   
# print(dir(my_list)) # it does not have __next__() method but has iter mathod
print(my_list.__iter__())  # <list_iterator object at 0x000002254C18FFD0>
# And the iterator that it returned from __iter__() method , it must define __next__() method whic access elements one at a time 
my_iterable=iter(my_list)  # same as my_list.__iter__()
# print(dir(my_iterable))   # iterator has both __iter__() method and __next__() method
print(my_iterable.__next__()) 
print(next(my_iterable)) 
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable)) #StopIteration
"""
Iterator is an object with the state remembers where it is at its iteration it knows how to fetch the next value using next() method ,
whn it doesnot have a next value it will throw an StopIteration Exception

"""

"""
Generators :   Generators are extremely useful to create easy to use iterators , they look like normal fucntion instaed returning a result 
they yield value , when they yield a vlaue they remember the state until the next value.

Generators are iterators as well but the __iter__() and __next__() method called automatically 



def my_gen(n):

    i=0
    while i<n:
        yield i
        i+=1

# gen_obj=my_gen(10)
for i in my_gen(11):
    print(i)
"""
