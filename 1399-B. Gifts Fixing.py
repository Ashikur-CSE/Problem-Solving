for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x=min(l1)
    y=min(l2)
    s=0
    for j in range(n):
        a=0
        b=0
        a=l1[j]-x
        b=l2[j]-y
        z=max(a,b)
        s=s+z
    print(s)