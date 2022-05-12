from math import floor
a,b=map(int,input().split())
if a>=b:
    a=a-b
    a=a/2
    x=floor(a)
    y=int(a)
    print(b,y)
elif b>a:
    b=b-a
    b=b/2
    m=floor(b)
    n=int(b)
    print(a,n)
    