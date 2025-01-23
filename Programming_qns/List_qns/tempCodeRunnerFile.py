Attendence = {
    "mon": [1, 2, 3, 4, 5],
    "tue": [1, 0, 3, 4, 0],
    "wed": [0, 2, 0, 4, 0],
    "thu": [1, 0, 0, 0, 5],
    "fri": [1, 2, 0, 0, 5],
}

from collections import Counter

mydict = {}
for key in Attendence:
    for num in Attendence[key]:
        if num != 0:
            mydict[key] = mydict.get(key, 0) + 1

print(mydict)
