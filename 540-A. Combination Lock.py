s=0
n=int(input())
l1= list(map(int,input()))
l2= list(map(int,input()))
for i in range(n):
    m=max(l1[i],l2[i])
    mi=min(l1[i],l2[i])
    s=s+min((abs(m-9)+mi+1),abs(l1[i]-l2[i]))
print(s)