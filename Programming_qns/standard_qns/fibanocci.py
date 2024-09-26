"""
Write a fibanocci series that generates and runs for infinite numbers


0,1,1,2,3,5,8
"""

def fibanocci(n):

    a=0
    b=1

    while n>0:  # True for infinite
        yield a
        a,b=b,a+b
        n-=1   #   ___
fib1=fibanocci(10)  # __ 


print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))

print(next(fib1))

print(next(fib1))

print(next(fib1))

print(next(fib1))


#*******************************************************************************************

# By recursive method

def fibanocci(n):

    # Base case 
    if n<=1:
        return n
    # Recursive case 
    return fibanocci(n-2) + fibanocci(n-1)

n=int(input("How many terms?"))
for i in range(n):
    print(fibanocci(i))


#chatgpt way
def fibonacci(n):
    sequence = [0,1]
    for i in range(2,n):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

print(fibonacci(10))



