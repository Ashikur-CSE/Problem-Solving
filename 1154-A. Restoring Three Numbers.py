list1=list(map(int,input().split()))
list1.sort()
c=list1[3]-list1[0]
b=list1[2]-c
a=list1[3]-(b+c)
print(a,b,c)