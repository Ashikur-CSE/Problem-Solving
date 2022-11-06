for i in range(int(input())):
    n=int(input())
    x=0
    while(x==0):
        if n%7==0:
            res=n
            x=1
        else:
            n=n+1
    print(n)
