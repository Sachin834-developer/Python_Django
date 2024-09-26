"""
    Q. Reverse the above string if the length of the word id greater
    than 5
    """
    
input1='reverse'
input2 = 'this is reversed string'
input3= 'all are word of goa'
    
def reverse_str(input_str):
    str_list = input_str.split()
    # print(str_list)
    output=[]
    for word in str_list:
        if len(word) >= 5:
            output.append(word[::-1])
        else:
            output.append(word)
            # print(output,'hii')
    return ' '.join(output)
            
print(reverse_str(input1))
print(reverse_str(input2))
print(reverse_str(input3))

