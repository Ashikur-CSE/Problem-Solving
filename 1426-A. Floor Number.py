for i in range (int(input())):
    
    n,x = map(int,input().split())
    s=2
    a=1
    if n==1 or n==2:
       a=a+0
    elif n>2:
       for i in range(1000):
        s=s+x
        a=a+1
        if s>=n:
            break
    print(a)