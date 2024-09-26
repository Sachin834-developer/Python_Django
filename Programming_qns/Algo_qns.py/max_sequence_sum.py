def max_sequence(lst):
    max_sum=0    
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            temp=sum(lst[i:j])
            print(temp)
            if temp > max_sum:
                seq=[]
                max_sum=temp
                seq.append(lst[i])
                seq.extend(lst[i+1:j])

    return f'{max_sum}:{seq}'
# lst=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
lst=[7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]  #155
# lst=[ 4, -1, 2, 1]  #  o/p =  6

# print(sum(lst[0:4]))
print(max_sequence(lst))