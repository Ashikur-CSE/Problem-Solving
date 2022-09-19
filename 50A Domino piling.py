m,n=map(int ,input().split())
res=None
if m>=1 and n<=16:
    print(int(m*n/2))
else:
    print(0)