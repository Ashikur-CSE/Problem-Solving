for i in range(int(input())):
    a,b,c=map(int,input().split())

    i=0
    maxAB = max(a,b)
    minAB=min(a,b)
    while(1):
        if(maxAB>c):
            break
        else:
            minAB=minAB+maxAB
            temp = minAB
            minAB=maxAB
            maxAB=temp
            i+=1
    print(i)
