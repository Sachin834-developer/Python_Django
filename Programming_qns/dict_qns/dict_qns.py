
string='apple ball animal cat dog donkey bat cow elphant'

"""
{ 
a:[apple,animal]
b:[ball,bat]
c:[cow,cat]
d:[dog,donkey]
e:[elephant]
}
"""
mylist=string.split()
mydict={}
for word in mylist:
    char=word[0]
    if char not in mydict:
        mydict[char]=[]
    mydict[char].append(word)
# print(mydict)

{print(k,':',v) for k ,v in mydict.items()}

input_dict={
'abhi':'TL',
'amit':'HR',
'akash':'TL',
'amv':'PM',
'sachin':'HR',
'guru':'TL',
'mani':'PM'
}

"""
OUTPUT
{
'TL':['abhi','akash','guru']
'HR':['amit','sachin']
'PM':['amv','mani']
}
"""

new_dict={}
for key,value in input_dict.items():
    if value not in new_dict:
        new_dict[value]=[]
    new_dict[value].append(key)

print(new_dict)