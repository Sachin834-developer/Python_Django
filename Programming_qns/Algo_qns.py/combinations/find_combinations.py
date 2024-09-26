from itertools import combinations

n=int(input())
s=input().split()
idx=int(input())

combinations_list=list(combinations(s,idx))
list1=[i for i in combinations_list if 'a' in i]
            
result= len(list1)/len(combinations_list)
    
print(result)