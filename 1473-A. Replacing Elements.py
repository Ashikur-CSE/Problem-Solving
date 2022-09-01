for i in range (int(input())):
    a,b=map(int,input().split())
    l1=sorted(list(map(int,input().split())))
    if l1[-1]<=b or l1[0]+l1[1]<=b:
        print("Yes")
    else:
        print("No")

