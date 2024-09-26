
for num in range(2,15):
    for  i in range(2,num):
        if num % i==0:
            break
    else:
        print(num,'is a prime number')


# for Range of numbers

import logging
import time

logger=logging.getLogger()
logging.basicConfig(level=logging.DEBUG,filename='test.log')
cur=time.time()
print(cur)
def gen_prime(start,end):
    logger.debug('Prime num gen starting from')
    for num in range(start,end):
        for i in range(2,num):
            if num%i==0 and num > 2:
                break
        else:
            print(num,'is a prime number')
            
start= int(input('Enter the start number :'))
end= int(input('Enter the end number :'))

gen_prime(start,end)