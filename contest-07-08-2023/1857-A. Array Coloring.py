for i in range(int(input())):
               
    n=int(input())
    l1=sorted(list(map(int,input().split())))
    if n>2:
        a=sum(l1[0:2])
        b=sum(l1[2:])
        if a%2==0 and b%2==0:
            print('YES')
        elif a%2!=0 and b%2!=0:
            print('YES')
        else:
            print('NO')
    elif n==2:
        if l1[0]%2==0 and l1[1]%2==0:
            print('YES')
        elif l1[0]%2!=0 and l1[1]%2!=0:
            print('YES')
        else:
            print('NO')


