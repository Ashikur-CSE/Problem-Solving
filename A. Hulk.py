n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        if n==1 or i==n:
            print("I hate it",end=" ")
        else:
            print("I hate that",end=" ")     
    else:
        if i==n:
            print("I love it",end=" ")
        else:
            print("I love that",end=" ")
        