for i in range(int(input())):
    n=int(input())
    c=0
    l1=list(map(int,input().split()))
    for i in range(n-1):
        mx=max(l1[i],l1[i+1])
        mn=min(l1[i],l1[i+1])
        while(mn*2<mx):
            c=c+1
            mn=mn*2
    print(c)
