# n=int(input())
# for i in range(n):
t=int(input())
b2=[0]
for j in range(t):
    a,b =map(int, input().split())
    if a<=10:
        b2.append(b)
    else:
        continue
    n=0
    if a<=10 and b>b2[j-1]:
        n=j+1
        print(n)
        print(b2[j-1])
        print(b2)
    else:
        continue
