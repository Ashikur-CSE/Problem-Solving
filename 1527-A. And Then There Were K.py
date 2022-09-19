nk=int(input())
x=0
l1=[]
for i in range(1,nk+1):
    l1.append(i)
l1.sort(reverse=True)
for i in l1:
    x=x&(i&i+1)
  
    print(x)

