for i in range(int(input())):
    a,b=map(int,input().split())
    if a>0:
        x=b*2
        y=a+x
        print(y+1)
    else:
        print(1)