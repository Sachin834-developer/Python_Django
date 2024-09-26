"""
Armstrong Number 

153 = 1 cube + 5 cube + 3 cube
153= 1 + 125 + 27

"""
# find the armstrong numbers below n
def is_armstrong(n):

    for i in range(n):
        temp=i
        sum=0
        while temp>0:
            digit = temp%10
            # print(digit)
            sum+=digit**3
            temp=temp//10
        if i==sum:
            print(i,' is a Armstrong Number')
      
n=int(input('Find the Armstrong numbers below :'))
is_armstrong(n)

# Optimized Version
def is_armstrong(num):
    res = sum(int(digit) **3 for digit in str(num))
    return res == num 

final_opt = [n for n in range(1,500) if is_armstrong(n)]
print(final_opt)