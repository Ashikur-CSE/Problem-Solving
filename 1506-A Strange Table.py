for i in range(int(input())):
    n,m,x=map(int,input().split())
    a=(x-1)%n
    b=(x-1)//n
    res=(m*a+b+1)
    print(res)