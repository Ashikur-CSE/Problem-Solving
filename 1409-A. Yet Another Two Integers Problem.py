t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=abs(a-b)
    res=x//10
    if x%10!=0:
        res=res+1
    print(res)
    
    
    
        
