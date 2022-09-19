for i in range (int(input())):
    n=int(input())
    l1=[]
    for i in range(1,n+1):
        l1.append(i)
    for j in range(len(l1)-1):
        l1[j-1], l1[j] = l1[j], l1[j-1]
    print(*l1)
