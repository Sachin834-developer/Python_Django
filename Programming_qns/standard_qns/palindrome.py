"""
check whether the  string is palindrome or not 



"""

my_string='malayalam'
my_string2='sachin'

# Using Sliciing
"""
def palindrome(str):
    temp_str=str[::-1]
    if str==temp_str:
        return f'{str},is a palindrome'
    else:
        return f'{str},is not a palindrome'
    
print(palindrome(my_string))
print(palindrome(my_string2))
"""

#Using For loop
def palindrome_2(str):
    for i in range (int(len(str)/2)+1):
        print(i)
        print(str[i],str[-i-1])
        if str[i]!=str[-i-1]:
            return f'{str},is not a palindrome'
    else:
        return f'{str},is a palindrome'

print(palindrome_2(my_string))
print(palindrome_2(my_string2))

#Prc1

my_str=input('Enter the String: ')
#Using Slicing
if my_str == my_str[::-1]:
    print(my_str,'is a Palindrome')
else:
    print(my_str,'is Not Palindrome')
    
# Using For Loop
for i in range(len(my_str)):
    if my_str[i]!=my_str[len(my_str)-i-1]:
        print(my_str,'is Not Palindrome')
        break
else:
    print(my_str,'is a Palindrome')
        
"""
'abcdef'


def reverse_str(input):
    return ''.join([input[-i] for i in range(1,len(input)+1)])

print(reverse_str('malayalama'))
"""
#Using WHile Loop
my_str= 'abcba'
n=len(my_str)
first=0
last=n-1
while n>=1:
    if my_str[first]!=my_str[last]:
        print(my_str,'is Not Palindrome')
        break
    first+=1
    last-=1
    n-=1
else:
    print(my_str,'is a Palindrome')

    
#Palindrome of a Number for a certain range 
def is_palindrome(start,end):
    for i in range(start,end):
        new_num=''
        temp=i
        while temp>0:
            digit=temp%10
            new_num+=str(digit)
            temp=temp//10
        if str(i)==new_num:
            print(i,'is a Palindrome')
        else:
            print(i,'is not a palindrome')

start=int(input("Enter the Number to start from  :"))
end=int(input("Enter the Number up to :"))

is_palindrome(start,end)

