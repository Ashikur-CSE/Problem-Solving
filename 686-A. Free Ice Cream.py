n,x=map(int,input().split())
m=0
for i in range(n):
    a,b=map(str,input().split())
    if a=="+":
        x=(x+int(b))
    elif int(b)<=x:
        x=(x-int(b))
    else:
        m+=1
print(x,m)

   
