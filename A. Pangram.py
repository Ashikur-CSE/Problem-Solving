n=int(input())
s=input()
l=s.lower()
list1 =list(l)
set1=set()
for i in range(n):
    if l[i]>="a" and l[i]<="z":
        set1.add(l[i])
z=len(set1)
if z==26:
    print("YES")
else:
    print("NO")