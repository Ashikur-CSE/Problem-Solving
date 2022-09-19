for i in range(int(input())):
    n,m=map(int,input().split())
    l1=[0,m]
    if n==2:
        print(m)
    elif n==1:
        print(0)
    else:
        print(2*m)