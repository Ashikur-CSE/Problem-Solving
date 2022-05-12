n,k=map(int,input().split())
res=240-k
count=0
sum =0
for i in range(1, n+1):
    z=5*i
    sum=sum+z
    if sum>res:
        break
    count=count+1
print(count)
    
