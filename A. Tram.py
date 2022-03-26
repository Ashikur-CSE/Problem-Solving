n=int(input())
x=[]
for i in range(n):
    y=list(map(int,input().split()))
    x.append(y)
person=0
max=0
for j in x:
    person=person-j[0]+j[1]
    if max<person:
        max=person
print(max)