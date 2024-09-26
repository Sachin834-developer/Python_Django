"""
Move the zeros to the end of the list

"""

def move_zeros(lst):
    
    non_zerolst=[i for i in lst if i!=0]
        
    return [0]*(len(lst)-len(non_zerolst))+ non_zerolst

lst=[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print(move_zeros(lst))

#without new list
"""
def move_zeros(lst):
    write_index=0
    for num in lst:
        if num !=0:
            lst[write_index]=num
            write_index+=1
    print(lst)
    while write_index < len(lst):
        lst[write_index] = 0
        write_index += 1
    print(lst)
"""
# lst=[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
lst=[9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros(lst))

