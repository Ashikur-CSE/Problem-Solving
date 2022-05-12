n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=[]
count=0

for i in x[1:]:
    if i not in z:
        if i>0:
            z.append(i)
for i in y[1:]:
    if i not in z:
        if i>0:
            z.append(i)
l=len(z)
if l<n:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")