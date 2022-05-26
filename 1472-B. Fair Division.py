for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(len(l1)):
        if l1[i]==1:
            c1=c1+1
        elif l1[i]==2:
            c2=c2+1
    if c1%2==1 or (c1==0 and n%2==1):
        print("NO")
    else:
        print("YES")