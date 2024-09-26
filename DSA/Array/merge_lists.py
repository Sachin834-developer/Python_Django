


# create opt as list beacause if its str concatination operation takes O(n) times with in the loop so it will be
# Time comp..  - O(n**2)


# Time : O(m+n)
# Space : O(m+n)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        opt = [] 
        w = word1 if len(word1) > len(word2) else word2
        count = 0
        for i,j in zip(word1,word2):
            opt.append(i)
            opt.append(j)
            count+=1
        opt.append(w[count:])
        
        return ''.join(opt)
"""
Time Complexity
Initialization:

opt = [] takes O(1).
w = word1 if len(word1) > len(word2) else word2 involves comparing the lengths of word1 and word2, which are 
O(1) operations.
count = 0 is 
O(1).

Loop Using zip:

The for loop for i, j in zip(word1, word2) iterates through both word1 and word2 up to the length of the shorter word. Let's denote the length of word1 as 
𝑛
n and word2 as 
𝑚
m.
Since zip stops at the shorter word, the loop runs 

min(n,m) times.
Inside the loop:
opt.append(i) and opt.append(j) are 

O(1) operations.
Therefore, this loop takes 

O(min(n,m)) time.
Appending the Remaining Part:

opt.append(w[count:]) appends the remaining substring of the longer word to the list. This is 

O(k) where 
k is the length of the remaining part. However, since 
k≤max(n,m), this operation is effectively 

O(n+m).
Join Operation:

''.join(opt) concatenates all the elements in opt into a single string. This operation takes 

O(n+m) time, where 
𝑛
n is the length of word1 and 
𝑚
m is the length of word2.
Total Time Complexity
The loop and the join operation together take 

O(n+m).
Therefore, the overall time complexity is: 

O(n+m)
Space Complexity
List Storage: The opt list stores all characters from both word1 and word2, which is 

O(n+m).
Final String: The joined string also takes 

O(n+m) space.
Therefore, the space complexity is: 

O(n+m)

Summary
Time Complexity: 

O(n+m) – Linear time, as the list operations and the join are efficient.
Space Complexity: 

O(n+m) – To store the merged result in the list and final string.
This is an efficient solution for merging the two strings alternately.

"""
        

        