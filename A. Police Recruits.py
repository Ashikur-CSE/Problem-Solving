n=int(input())
x=list(map(int,input().split()))
p=0
c=0
for i in range(len(x)):
    if x[i]>0:
        p=p+x[i]
    else:
        if p<1:
            c=c+1
        else:
            p=p-1
print(c)
        

