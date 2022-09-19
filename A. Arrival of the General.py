from re import I


n=int(input())
x=list(map(int,input().split()))
m=0
k=101

for i in range(n):
    if x[i]>m:
        m=x[i]
        ma=i
    if x[i]<=k:
        k=x[i]
        mi=i
if ma>mi:
    mi=mi+1
print(ma+(n-1)-mi)

