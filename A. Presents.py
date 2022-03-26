n=int(input())


x=list(map(int,input().split()))
i=1   
for j in range(n):
    x[j]=i
    i=i+1
for i in range(n):
    print(x[i])


