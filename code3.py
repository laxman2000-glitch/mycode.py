def fednoies(n):
    if n < 0:
        print ("negative values are not allowed")
        return
    a=0
    b=1
    if n == 0:
        print(0)
        return
    elif n == 1:
        print(0)
        print(1)
        return
    
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    if c < 100:
        print(c, end=",")
        else:
            break
n = int(input("give the number"))
fednoies(n)
