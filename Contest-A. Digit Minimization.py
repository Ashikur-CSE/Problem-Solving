t=int(input())
for i in range(t):
    l1=list(map(int,input()))
    l=len(l1)
    if l==2:
        print(l1[1])
    else:
        print(min(l1))