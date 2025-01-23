"""
1st round Python Developer
Sakathiya Technologies Jan 17 2025

Reverse the string except special chars

inp_str = "a,sjh$xyz"
# opt = "z,yxh$jsa"

    """

inp_str = "a,sjh$xyz"
# opt = "z,yxh$jsa"
print(list(inp_str))
chars_list = [char for char in inp_str if char.isalpha()][::-1]
print(chars_list)
res = ""
index = 0
for char in inp_str:
    if not char.isalpha():
        res += char
    else:
        res += chars_list[index]
        index += 1
print(res)
