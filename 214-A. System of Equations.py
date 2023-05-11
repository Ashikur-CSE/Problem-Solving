m,n=map(int,(input().split()))
c=0
for a in range(n+1):
    b=n-a**2
    if b>=0:
        if a+b**2==m:
            c=c+1
print(c)