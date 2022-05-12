n=int(input())
x=[]
for i in range(n):
    x.append(input())
templist=x[0]
count=1
for j in range(1,n):
    if x[j]!=templist:
        templist=x[j]
        count+=1
print(count)
    