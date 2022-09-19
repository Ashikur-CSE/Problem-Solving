t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=max(a,b)
    y=min(a,b)
    if x>=2*y:
        print(x*x)
    else:
        print((2*y)*(2*y))