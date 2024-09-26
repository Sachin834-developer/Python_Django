inp=[[2, 6],[1, 3],[8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

def merge_intervals(inp):
    output=[]
    inp.sort(key=lambda x:x[0])
    print(inp)
    for i in range(len(inp)-1):
        if inp[i][1] > inp[i+1][0]:
            output.append([inp[i][0],inp[i+1][1]])
        else:
            output.append(inp[i+1])
    # output.append(inp[i+1])
    return output

print(merge_intervals(inp))