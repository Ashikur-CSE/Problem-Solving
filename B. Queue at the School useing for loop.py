n,x=map(int,input().split())
s=input()
list1 = list(s)
w=0
for j in range(0<x):
    for i in range(n-2):
        w=i
        if list1[i]=="B" and list1[i+1]=="G":
            list1[i]="G"
            list1[i+1]="B"
            w=i+1
        w=i+1
print(list1)


