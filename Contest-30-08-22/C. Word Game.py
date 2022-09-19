n=int(input())
l1=list(map(str,input().split()))
l2=list(map(str,input().split()))
l3=list(map(str,input().split()))
a=0
b=0
c=0
for i in range(n):
    if l1[i] in l2 and l1[i] in l3:
        a=0
        b=0
        c=0
    elif l1[i] in l2:
        a=a+1
        b=b+1
    elif l1[i] in l3:
        a=a+1
        c=c+1
    elif l2[i] in l3:
        b=b+1
        c=c+1
    elif l2[i] in l1:
        a=a+1
        b=b+1
    elif l1[i] not in l2 and l3:
        
        


