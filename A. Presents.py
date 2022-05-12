n= int(input())

x = list(map(int, input().split()))

for i in range (1, n+1):
    for j in range (n):
        if i==x[j]:
            print(j+1,end=" ")