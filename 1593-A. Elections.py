for i in range(int(input())):
    a,b,c=map(int,input().split())
    print(max(a,b+1,c+1)-a,max(a+1,b,c+1)-b,max(a+1,b+1,c)-c)