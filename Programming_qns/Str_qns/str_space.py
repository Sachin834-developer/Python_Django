list1=['car','ca t','be  ar','mat er ial']
output ={}
for word in list1:
    if ' ' not in word:
        output[word] = 0
    for char in word:
        if char == ' ':
            if word not in output.keys():
                print(word)
                output[word] = 1
            else:
                output[word]+=1
    # else:
    #     output[word]=0
    # if ' ' in word:
    #     output.append(True)
    # else:
    #     output.append(False)
print(output)
