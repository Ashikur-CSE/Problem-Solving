for i in range (int(input())):
    e=0
    o=0
    n=int(input())
    a= list(map(int,input().split()))
    for i in a:
        if i%2==0:
            e+=1
        else:
            o+=1
    x=sum(a)
    if x%2==1:
        print("YES")
    elif e>=1 and o>=1:
        print("YES")
    else:
        print("NO")