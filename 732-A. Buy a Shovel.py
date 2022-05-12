x,y=map(int,input().split())
sum=0
for i in range(1,50):
    z=x*i
    div=z//10
    if z==(div*10+y):
        break
    elif z==(div*10):
        break
print(i)