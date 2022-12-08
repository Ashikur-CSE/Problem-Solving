for i in range(int(input())):
    l1=list(map(int,input().split()))
    for i in range(len(l1)):
        for j in range(len(l1)-i-1):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
    print(l1[1])
        