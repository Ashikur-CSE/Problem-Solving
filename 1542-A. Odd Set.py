for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    o=0
    e=0
    for i in l1:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e==o:
        print("YES")
    else:
        print("NO")
