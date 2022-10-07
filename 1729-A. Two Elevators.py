for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=abs(a-1)
    y=abs(b-c)
    z=abs(c-1)
    r=(y+z)
    if x<r:
        print(1)
    elif x==r:
        print(3)
    else:
        print(2)
