for i in range(int(input())):
    c=0
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]>a[0]:
            c=c+1
    print(c)