for i in range (int(input())):
    l3=[]
    l2=[]
    n=int(input())
    l1=list( map(int,input().split()))
    l=len(l1)
    for i in range(n//2):
        l3.append(l1[i])
        l3.append(l1[l-1])
        l=l-1
    if n%2!=0:
        l3.append(l1[(n//2)])
    s = [str(i) for i in l3] 
    result = str(" ".join(s)) 
    print(result)
    