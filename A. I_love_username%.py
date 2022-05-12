n=int(input())
x=list(map(int,input().split()))
max=x[0]
min=x[0]
count=0
for i in range(n):
    if x[i]>max:
        max=x[i]
        count=count+1
    elif x[i]<min:
        min=x[i]
        count=count+1
print(count)
