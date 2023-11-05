for i in range(int(input())):
    a,b,c,x,y=map(int, input().split())
    if a>=x and b>=y:
        print("YES")
    elif a>=x and b<y:
        n=abs(b-y)
        if n>=c:
            print("YES")
        else:
            print("NO")
    elif b>=y and a<x:
        m=abs(a-x)
        if m>=c:
            print("YES")
        else:
            print("NO")
    elif a<x and b<y:
        p=abs(a-x)
        q=abs(b-y)
        l=p+q
        if l<=c:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

