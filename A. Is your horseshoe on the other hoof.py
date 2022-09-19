n=list(map(int,input().split()))
x=[]
for i in n:
    if i not in x:
        x.append(i)
res=len(n)-len(x)
print(res)