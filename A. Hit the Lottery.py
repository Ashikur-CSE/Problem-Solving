n=int(input())
a=[100,20,10,5,1]
count=0
for i in range(len(a)):
    x=n/a[i]
    n=n%a[i]
    count=count+int(x)
print(count)