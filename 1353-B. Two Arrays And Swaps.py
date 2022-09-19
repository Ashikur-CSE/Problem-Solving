t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort(reverse=True)
    for i in range(k):
        if l1[i]<l2[i]:
            l1[i],l2[i]=l2[i],l1[i]
    print(sum(l1))