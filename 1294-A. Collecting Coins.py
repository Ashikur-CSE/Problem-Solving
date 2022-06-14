for i in range(int(input())):  
    a,b,c,d=map(int,input().split())
    x=max(a,b,c)
    j=x-a
    k=x-b
    l=x-c
    m=j+k+l
    n=d-m
    if n<0:
        print("NO")
    elif n%3==0:
        print("YES")
    else:
        print("NO")