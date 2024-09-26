mylist=[[1,2,3],[3,4,5,6],[7,5,8,5,3]]

max_length=0
for sublist in mylist:
    if len(sublist)>max_length:
        max_length=len(sublist)

# print(max_length)
for i in range(max_length):
    output=[]
    for sublist in mylist:
        if len(sublist)>i:
            output.append(sublist[i])
        
    print(','.join(str(i) for i in output))
    
