n=int(input())
x=[]
count=0
for i in range(n):
    y=list(map(int,input().split()))
    x.append(y)
for j in x:
    if j[0]==j[1]:
        count=count+0
    elif j[0]+1<j[1]:
        count=count+1
print(count)