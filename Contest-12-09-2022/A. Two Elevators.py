for i in range(int(input())):
    a,b,c=map(int,input().split())

    x=abs(a-1)
    if b<c:
        m=abs(b-c)
        n=abs(m-a)
    elif b>c:
        n=(b-c)
    z=min(x,n)
    if z==0:
        print(1)
    elif x!=n:
        print(2)
    else:
        print(3)