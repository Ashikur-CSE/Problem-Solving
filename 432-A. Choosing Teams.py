n,k=map(int,input().split())
list1=list(map(int,input().split()))
count=0
for i in range(n):
    x=5-k
    if list1[i]<=x:
        count=count+1
print(count//3)
