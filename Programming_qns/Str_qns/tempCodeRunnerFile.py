
from itertools import combinations,permutations

# print(list(combinations(['a','b','c'],2)))
perms=list(permutations(['a','b','c'],3))
output=[]
for tup in perms:
   output.append(''.join(tup))
print(output)