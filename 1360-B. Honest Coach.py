t=int(input())
for i in range(t):
    x=int(input())
    l1=sorted(map(int,input().split()))
    l2=[]
    for i in range(1,x):
        z=(l1[i]-l1[i-1])
        l2.append(z)
    print(min(l2))
    #print(min(l1[p]-l1[p-1] for p in range(1,x)))
