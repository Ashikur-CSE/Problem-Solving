for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    if list(set(a)) == a:
        print(len(a))
    else:
        c=len(set(a))-len(a)
        if c%2==0:
            print(len(set(a)))
        else:
            print(len(set(a))-1)
        
