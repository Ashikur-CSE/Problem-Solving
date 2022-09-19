X=0
n=int(input())

for i in range(0,n):
    z=input()
    if "++" in z:
        X=X+1
    else:
        X=X-1
print(X)
