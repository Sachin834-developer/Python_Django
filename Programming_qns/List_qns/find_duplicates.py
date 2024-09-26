list1 = [1,2,3,3,4,4]

def find_duplicates(list1):
    seen = set()
    duplicates = set()
    for num in list1:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(find_duplicates(list1))