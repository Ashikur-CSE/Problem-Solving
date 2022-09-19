n=int(input())
list1=list(map(int,input().split()))
z=max(list1)
count=0
for i in range(n):
    count+=z-list1[i]
print(count)


