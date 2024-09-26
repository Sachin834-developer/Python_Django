def star_pyramid(n):
    k = n-1
    for i in range(n):


        for j in range(k):
            print(end=" ")
        
        k -=1

        for m in range(i+1):
            print("* ",end="")

        print('\r')
star_pyramid(5)


