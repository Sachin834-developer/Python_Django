"""
FInd the factorial of a number using recursion.

Recursion is calling the function inside the function itself.

5! = 5*4!
4! = 4*3!
3! = 3*2!  = 3* 2  = 6 
2! = 2*1!    2* 1  = 2
1! = 1* 0!   =1*1    =1
0! = 1               = 1


"""
def factorial(number):
    if number <=1:
        return number
    return number * factorial(number-1)

print(factorial(5))

"""
Fibanocci using recursion

0,1,1,2,3,5,8

Print the n fibanocci numbers

Base case : its where the recusion stops  and general case : recursive function looop


    """

# Fact witout recursion

n=5
sum=1
for i in range(1,n+1):
    sum = sum*i
print(sum)

from math import factorial
def find_factorial(n):
    result = 1
    for digit in range(1,n+1):
        result= result * digit
    return result
print(find_factorial(2))
print(factorial(2))


# for range of numbers

def find_factorial(start,end):
    for n in range(start,end):
        res=1
        if n==1 or n==0:
            print('factorial of ',n, 'is',n)
        else:
            for num in range(1,n+1):
                res=res*num
            print('factorial of ',n, 'is',res)

find_factorial(1,10)
        