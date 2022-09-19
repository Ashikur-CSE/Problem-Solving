for i in range(int(input())):
    n=int(input())
    
    if n%3==1:
        a1=(n//3)+1
        a2=a1-1
    elif n%3==2:
        a1=(n//3)
        a2=a1+1
    elif n%3==0:
        a1=(n//3)
        a2=a1
    print(a1,a2)


