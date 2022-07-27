for i in range (int(input())):
    n=int(input())
    l1= list(map(int,input().split()))
    x=sum(l1)
    if x%2==0:
        print("NO")
    else:
        print("YES")
