for i in range(int(input())):
    n=int(input())
    c=0
    l1=list(map(int,input().split()))
    x=min(l1)
    for j in l1:
        c=c+(j-x)
    print(c)