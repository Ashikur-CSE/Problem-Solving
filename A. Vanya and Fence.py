n,h=map(int,input().split())
x=list(map(int,input().split()))
count=0
for i in x:
    if i>h:
        count=count+2
    else:
        count=count+1
print(count)