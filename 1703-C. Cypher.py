for i in range(int(input())):
    n=int(input())
    l1= list(map(int,input().split()))
    p=0
    l2=[]
    for i in range(n):
        x=l1[p]
        n,m = map(str,input().split())
        for j in range(len(m)):
            if m[j]=="D":
                x=x+1
                if x==10:
                    x=0
            else:
                x=x-1
                if x==-1:
                    x=9
        p=p+1
        l2.append(x)

    s = [str(i) for i in l2] 
    result = str(" ".join(s)) 
    print(result)
