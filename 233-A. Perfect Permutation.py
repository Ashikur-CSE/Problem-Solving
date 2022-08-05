n=int(input())
l1=[]
if n%2==0:
    for i in range(1,n+1):
        l1.append(i)
    for j in range(n,0,-1):
        print(j,end=" ")
else:
    print(-1)

