

def fibanocci(n):
    if n <= 1:
        return n
    return fibanocci(n-1) + fibanocci(n-2)

for i in range(10):
    print(fibanocci(i))