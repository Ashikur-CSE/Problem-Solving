for i in range(int(input())): 
    n=int(input())
    x=0
    i=0
    while(x<n):
        x=(10**i)
        i=i+1
    z=i-2
    if x==n:
        s=0
    elif z<0:
        s=abs(1-n)
    else:
        s=abs(n-(10**z))
    print(s)

    
