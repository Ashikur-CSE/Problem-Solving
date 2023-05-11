for i in range(int(input())):
    import math
    n=int(input())
    if n==1:
        print(2)
    elif n==2:
        print(1)
    elif n>2:
        x=math.floor(n/3)
        a=x*3
        if a==n:
            print(x)
        else:
            print(x+1)