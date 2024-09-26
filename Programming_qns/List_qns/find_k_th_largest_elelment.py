inp_lst = [2,4,8,9,3,5,7,8,10]

"""
find the kth largest element from the list 
"""

# BUBBLE SORTING ALGORITHM

def bubble_sort(arr):
    n =len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

    return arr
arr = [2,4,6,8,3,5,7,9]
print(bubble_sort(arr))

def find_k_th_largest_elelment(arr,k):
    n = len(arr)

    for i in range(n):
        print(0,n-i-1)
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    
    return arr[-k]

print(find_k_th_largest_elelment(inp_lst,2))
            




