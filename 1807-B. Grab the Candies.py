for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    m=0
    b=0
    for i in l1:
        if i%2==0:
            m=m+i
        else:
            b=b+i
    if m>b:
        print("YES")
    else:
        print("NO")
