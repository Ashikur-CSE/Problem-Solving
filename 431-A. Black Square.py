l1=list(map(int,input().split()))
l2=list(map(int,input()))
sum=0
for i in range(len(l2)):
    a=(l2[i])-1
    sum=sum+l1[a]
print(sum)
