for j in range(int(input())):
    n=int(input())
    s=input()
    x=0
    y=0
    r=0
    for i in s:
        if i=='U':
            y=y+1
        elif i=='D':
            y=y-1
        elif i=='L':
            x=x-1
        elif i=='R':
            x=x+1
        if x==1 and y==1:
            r=r+1
    if r>=1:
        print("YES")
    else:
        print("NO")

                    