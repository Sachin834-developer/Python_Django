input_str='cat rat bat mat cat rat put cut cat cut put rat bat bat bat'
number=int(input('How many times the word should be repeated? '))

input_list=input_str.split()
my_dict={}
for word in input_list:
    if word not in my_dict:
        my_dict[word]=0
    my_dict[word]+=1

my_str=''
for key,value in my_dict.items():
    if value == number:
        my_str+= key+' '
print(my_str)

"""
my_dict={}
for char in b:
    if char not in my_dict.keys():
        my_dict[char]=0
    my_dict[char]+=1

for char in b:
    my_dict[char]=my_dict.get(char,0)+1
print(my_dict)
 """
# print(set(input_list)) rough
# using dict comprenhsion
inp_list =input_str.split()
opt_dict = {word:inp_list.count(word) for word in inp_list}
print(opt_dict)