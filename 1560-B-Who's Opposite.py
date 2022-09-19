for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=abs(a-b)
    y=x*2
    if y<a or y<b or y<c:
        print(-1)
    elif c<=x:
        print(x+c)
    else:
        print(abs(x-c))