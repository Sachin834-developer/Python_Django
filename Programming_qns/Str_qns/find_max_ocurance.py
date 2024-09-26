"""
Find the max occrance of string ?

"""
#v with words 
my_str='if but put hat put it but hat it but cat rat cat'

new_list=my_str.split()

my_dict={}

for word in new_list:
    if word not in my_dict:
        my_dict[word]=1
    else:
        my_dict[word]+=1

# print(my_dict)
name='shantosh'
#01234567
print(name[6:2:-2])
# for chars 

my_str2='sahhjdjsahjahdjhjsahdjsahdhHAHDASHJH'
my_str2=my_str2.lower()

my_dict2={}

for char in my_str2:
    if char in my_dict2.keys():
        my_dict2[char]+=1
    else:
        my_dict2[char]=1

for key,value in my_dict2.items():
    print(f'{key} occured {value} times.')

{print(f'{key} occured {value} times.') for key,value in my_dict2.items()}