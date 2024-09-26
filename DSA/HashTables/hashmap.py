def get_hash_value(key):
    h=0
    for char in key:
        h+=ord(char)
    return h % 10
# print(get_hash_value('sachin'))    #0

class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def __getitem__(self,key):
        h = get_hash_value(key=key)
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h=get_hash_value(key=key)
        found = False
        for index,element in enumerate(self.arr[h]):
                if len(element) ==2 and element[0] == key:
                     self.arr[h][index] == (key,val)
                     found = True

        if not found:
             self.arr[h].append((key,val))
    def __delitem__(self,key):
         h = get_hash_value(key=key)
         for index,element in enumerate(self.arr[h]):
              if element[0] == key:
                   del self.arr[h][index]
                   break

if __name__=='__main__':
    t = HashTable()
    t['march 6'] = '100'
    t['march 17'] = '200'
    print(t['march 17'])
    del t["march 6"]
    print(t.arr)
