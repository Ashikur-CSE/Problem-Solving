n=int(input())
for i in range(n):
    temp=[]
    x=int(input())
    count=x
    temp=list(map(int,input().split()))
    temp.sort()
    for j in range(x-1):
        if (temp[j]==temp[j+1]):
            count=count-1
        elif (abs(temp[j]-temp[j+1]))<=1:
            count=count-1
    if count==1:
        print("YES")
    else:
        print("NO")
