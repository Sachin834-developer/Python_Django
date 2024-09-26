"""
Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)

""" 
inp_str=input()
sub_str=input()

start=0
end=len(sub_str)

out=[]
[out.append((i,i+1)) for i in range(len(inp_str)) if sub_str == inp_str[i:i+2]]
print(out)
# temp=len(inp_str) - (end-1)
# while temp>0:
#     if sub_str == inp_str[start:end]:
#         print((start,end-1))
#     start+=1
#     end+=1
#     temp-=1
        
for i in range((len(inp_str)-end)+1):
    if sub_str==inp_str[i:end]:
        print((i,end-1))
    end+=1

# ---------------------OR----------------------
for i in range(len(inp_str)-1):
    if inp_str[i:i+2] == sub_str:
        print(i,',',i+1)