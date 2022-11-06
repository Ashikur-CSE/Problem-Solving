for i in range (int(input())):
    n=int(input())
    l1=list(map(int,input().split()))

    l2=set(l1)
    if len(l2)==n:
        print("YES")
    else:
        print("NO")
    
