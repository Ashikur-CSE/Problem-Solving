n=int(input())
m=0
c=0
for i in range(n):
    l1=list(map(int,input().split()))
    for i in range(len(l1)):
        
        if l1[0]>l1[1]:
            m=m+1
        elif l1[1]>l1[0]:
            c=c+1
        else:
            m+=0
            c+=0
if m>c:
    print("Mishka")
elif c>m:
    print("Chris")
else:
    print("Friendship is magic!^^")