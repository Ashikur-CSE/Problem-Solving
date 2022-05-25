t=int(input())
for i in range(t):
    a=0
    c=0
    j=0
    k=int(input())
    for i in range(1,1667):
        if i%3!=0 and i%10!=3 :
            a=i
            c=c+1
            if c==k:
                break
    print(a)