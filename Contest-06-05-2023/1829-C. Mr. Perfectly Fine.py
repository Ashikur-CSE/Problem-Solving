for _ in range(int(input())):
    n=int(input())
    a=0
    b=0
    l1=[]
    l2=[]
    l3=[]
    t=[]
    t2=[]
    t3=[]
    x=0
    tmin1=0
    tmin2=0
    tmin=0
    for i in range(n):
        a,b = input().split()
        l1.append(a)
        l1.append(b)
    for j in range(len(l1)):
        if j%2==0:
            l2.append(l1[j])
        elif j%2!=0:
            l3.append(l1[j])
    for k in range(len(l3)):
        if l3[k]=='11':
            t.append(int(l2[k]))
            tmin=min(t)
            x=1
        elif x==0:
            if l3[k]=='10':
                t2.append(int(l2[k]))
                tmin1=min(t2)
            elif l3[k]=='01':
                t3.append(int(l2[k]))
                tmin2=min(t3)
                tmin=tmin1+tmin2
        else:
            tmin=-1    
    print(tmin)

