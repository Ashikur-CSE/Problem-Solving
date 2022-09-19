n=int(input())
al=[]
bl=[]
count=0
for i in range(n):
    a,b=map(int,input().split())
    al.append(a)
    bl.append(b)
for i in range(len(al)):
    for j in range(len(al)):
        if al[i]==bl[j]:
            count=count+1
print(count)

