for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    x=sum(l1)
    if n>x:
        print(1)
    else:
        print(x-n)

