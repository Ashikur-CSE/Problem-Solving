for i in range (int(input())):
    s=list(input())
    l2=[]
    
    if len(s)%2==0:
        l=int(len(s)/2)
        for i in range(l):
            l2.append(s[i])
        for j in range(l):
            s.remove(s[0])
        if s==l2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")