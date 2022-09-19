for i in range (int(input())):
    a,b = map(int,input().split())
    if a == b:
        print(0)
    elif (a>b and (a-b) % 2 ==0) or (a<b and (b-a) % 2 !=0):
        print(1)
    else:
        print(2)

"""for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        if a%2!=0:
            x=a-b
            if x%2==0:
                print(1)
            else:
                if x>1:
                    print(2)
                else:
                    print(1)
        else:
            if x>1:
                print(2)
            else:
                print(1)
    elif b>a:
        if a%2==0:
            y=b-a
            if y%2!=0:
                print(1)
            else:
                if y>1:
                    print(2)
                else:
                    print(1)
        else:
            y=b-a
            if y>1:
                print(2)
            else:
                print(1)
    elif a==b:
        print(0)"""




