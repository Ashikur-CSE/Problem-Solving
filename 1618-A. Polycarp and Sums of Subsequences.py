for i in range(int(input())):
    l1=list(map(int,input().split()))
    x=max(l1)
    a=l1[0]
    b=l1[1]
    c=x-(a+b)
    print(a,b,c)