n=int(input())
x=[]
for i in range(n):
    y=int(input())
    x.append(y)
l = ''.join(map(str, x))
count=0
for j in l:
    if l[j]=="01" or l[j]=="10":
        count=count+1
print(count)

    
    