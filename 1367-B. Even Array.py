t=int(input())
for i in range(t):
    n= int(input())
    l1=list(map(int,input().split()))
    odd=0
    even=0
    ok=0
    for i in range(n):
        if i%2==0:  
            if l1[i]%2==0:
                ok+=1
            else:
                even+=1
        else:
            if l1[i]%2==1:
                ok+=1
            else:
                odd+=1
    if ok==n:
        print(0)
    elif odd==even:
        print(even)
    else:
        print(-1)