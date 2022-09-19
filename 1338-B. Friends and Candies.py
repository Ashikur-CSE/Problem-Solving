for i in range (int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    s=sum(l1)
    if s%n!=0:
        print(-1)
    else:
        s2=s//n
        c=0
        for i in l1:
            if i>s2:
                c=c+1
        print(c)