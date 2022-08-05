n=input()
x = y = z = 0
l1=map(int, input().split())
for i in l1:
    if i > y:
        x=x+1 
    else:
        x=1
    y = i
    z = max(z, x)
print(z)
