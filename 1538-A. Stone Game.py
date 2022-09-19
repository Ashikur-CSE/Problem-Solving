for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    a=l1.index(min(l1))
    b=l1.index(max(l1))
    c=min(a,b)
    d=max(a,b)
    print(min(d+1,c+n+1-d,n-c))