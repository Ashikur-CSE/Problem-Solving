n=int(input())
l1=list(map(int,input().split()))
p=0
q=0
for i in range(n):
    b=max(l1[0],l1[-1])
    if i%2==0:
        p=p+b
    else:
        q=q+b
    l1.remove(b)
print(p,q)