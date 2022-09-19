for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=max(a,b)
    p=min(a,b)
    y=max(c,d)
    q=min(c,d)
    z=min(x,y)
    if z>p and z>q:
        print("Yes")
    else:
        print("NO")