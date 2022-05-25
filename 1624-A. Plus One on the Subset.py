for i in range(int(input())):
    n= int(input())
    l1=list(map(int,input().split()))
    print(max(l1)-min(l1))