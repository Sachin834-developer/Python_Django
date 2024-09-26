# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
word1  = ["abc", "d", "defg"]
# word2 = ["abcddefg"]
import time
def decorator_func(func):
    
    def wrapper(lst):
        start_time = time.time() 
        time.sleep(2)
        result = func(lst)
        end_time = time.time()
        print(end_time,start_time)
        act_time = end_time-start_time

        return result,act_time
    return wrapper



# word1 = ["a", "cb"]
word2 = ["ab", "c"]

@decorator_func
def merge_string(lst:list):
    res=''
    for char in lst:
        res+=char
    return res
      
print(merge_string(word1))
print(merge_string(word2))  
