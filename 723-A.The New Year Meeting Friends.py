list1=list(map(int,input().split()))
list1.sort()
x=abs(list1[1]-list1[0])
y=abs(list1[1]-list1[2])
print(x+y)