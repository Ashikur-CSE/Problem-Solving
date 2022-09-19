n=int(input())
str=input()
x=list(str)
count=0
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        count=count+1
    else:
        continue
print(count)