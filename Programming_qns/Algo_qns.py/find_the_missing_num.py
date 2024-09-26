

#Find the position of the missimng num in sorted array.
# find the position of the number , if the  number is present in a array.

arr=[1,2,4,5,6,7]
target = 3

def binary_search(arr,n):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = left + (right-left) // 2

        if n == arr[mid]:
                return mid
        elif arr[mid] < n:
             left = mid+1
        else:
             right = mid -1
    return left
print(binary_search(arr,target))
             

     
    
    
    