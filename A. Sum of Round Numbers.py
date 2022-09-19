n=int(input())
x=[]
for i in range(n):
    x.append(int(input()))
for i in range(n):
    temp=[]
    count=0
    if x[i]>=10000 and x[i]%10000==0:
        print(1)
        print(x[i])
    if x[i]<=10:
        print(1)
        print(x[i])
    if x[i]>10 and x[i]<10000:
        if x[i]%10!=0:
            ans=x[i]%10
            x[i]=x[i]-ans
            temp.append(ans)
        if x[i]%100!=0:
            ans=x[i]%100
            x[i]=x[i]-ans
            temp.append(ans)
        if x[i]%1000!=0:
            ans=x[i]%1000 
            x[i]=x[i]-ans
            temp.append(ans)
        if x[i]%10000!=0:
            ans=x[i]%10000
            x[i]=x[i]-ans
            temp.append(ans)
        print(len(temp))
        print(' '.join(str(x) for x in temp))
