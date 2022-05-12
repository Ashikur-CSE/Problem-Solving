t = int(input())
count=0
for i in range(t):
    a, b = map(int, input().split())
    if a%b==0:
        print(0)
    else:
        print(b-(a%b))
    
    