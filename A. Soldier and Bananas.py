k,n,w=map(int,input().split())
sum=0
i=1
for i in range(w+1):
    res=i*k
    sum=sum+res
ans=sum-n
if ans >0:
    print(ans)
else:
    print(0)
