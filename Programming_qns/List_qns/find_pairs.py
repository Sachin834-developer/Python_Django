"""
Find the Pair with given number in a list
#from the given list , find the matching sum of two numbers in a list comparing with the given number

"""
my_list=[0,2,4,5,8,4,1,4,5,1,6,2,1,4,5]



def find_pair(number):

    pair_list=[]
    # Using List Comprehension
    [pair_list.append((my_list[i],my_list[j])) 
     for i in range(len(my_list)) 
     for j in range(i+1,len(my_list)) 
     if my_list[i]+my_list[j]==number]
    
    # for i in range(len(my_list)):
    #     for j in range(i+1,len(my_list)):
    #         print(my_list[i],my_list[j])
    #         if my_list[i]+my_list[j]==number:
    #             pair_list.append((my_list[i],my_list[j]))

    return pair_list

print(find_pair(12))


#effiecent way

my_list=[0,2,4,5,8,4,1,4,5,1,6,2,1,4,5]


def find_pairs(lst,target):
    seen = set()
    pairs = set()
    for num in lst:
        bal = target - num
        if bal in seen:
            pairs.add(tuple((min((bal,num)),max(bal,num))))
        seen.add(num)
    return pairs

print(find_pairs(my_list,10))

