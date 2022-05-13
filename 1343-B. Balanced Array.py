t=int(input())
for i in range(t):
    n=int(input())
    n2=n/2
    if n%4!=0:
        print("NO")
    else:
        a=0
        b=0
        print("YES")
        for j in range(2,n+1,2):
            print(j,end=" ")
            a=a+j
        for k in range(1,n-1,2):
            print(k,end=" ")
            b=b+k
        print(a-b)