n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0

for i in range(0,n):
    if a[i]==0 and a[i]==a[k-1]:
        count=count+0
    elif a[i]==a[k-1] or a[i]>=a[k-1]:
        count=count+1
    else:
        count=count+0
print(count)





 
