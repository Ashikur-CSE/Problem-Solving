t=int (input())
for i in range(t):
    b=0
    x,y,n=map(int,input().split())
    a=n%x
    if a>y:
        print(n-a+y)
    elif a==y:
        print(n)
    elif y>a:
        print(n-a-x+y)
    """j = 2
    while j <= n:
        a=j%x
        if a == y:
            b=j
        j += 1
    print(b)"""
    """for j in range(2,n+1):
        a=j%x
        if a==y:
            b=j
    print(b)"""
            