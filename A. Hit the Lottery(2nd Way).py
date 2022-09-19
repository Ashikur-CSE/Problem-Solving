n=int(input())
count=0
x = n/100
left = n%100
count=count+x

x= left/20
left= left%20
count=count+int(x)
 
x= left/10
left = left%10
count=count+int(x)
 
x= left/5
left=left%5
count=count+int(x)
 
x=left/1
count=count+int(x)
print(int(count))