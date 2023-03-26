for i in range(int(input())):
    s=input()
    l=0
    l1=["c","o","d","e","f","o","r","c","e","s"]
    for j in range(0,len(l1),1):
        if l1[j]==s:
            l=l+1
        else:
            l=l+0
    if l>=1:
        print("YES")
    else:
        print("NO")