"""
find the substrings of the string

'abc'
bca,cab,acb

"""
def str_per(str,index=0):

    if index==len(str):
        print(''.join(str))


    for i in range(index,len(str)):
        wlist=[i for i in str]

        wlist[index],wlist[i]=wlist[i],wlist[index]
        str_per(wlist,index+1)

str_per('abc')



from itertools import combinations,permutations

# print(list(combinations(['a','b','c'],2)))
perms=list(permutations(['a','b','c'],3))
output=[]
for tup in perms:
   output.append( ''.join(tup))
print(output)


    

