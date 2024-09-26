"""
Input :  'Sky is blue"
output : 'blue is sky'


input='remove! punctuations# from@ me% and don't remove spaces/'

"""

#1.
my_str = 'Sky is blue'

new_list=my_str.split()  # returns list 
new_list=new_list[::-1]
new_str=' '.join(new_list)
print(new_str)

# In a line  
# my_str2=' '.join(my_str.split()[::-1])


#2.
input="remove! punctuations# from@ me% and don't remove spaces/"

punctuations= ['@','#','!','%','/']
for str in input:
    if str in punctuations:
        input=input.replace(str,'')
print(input)
