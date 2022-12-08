for i in range (int(input())): 
    n=int(input())
    s=input()
    on=0
    zer=0
    for i in range(n):
        if s[i]=="1":
            on=on+1
        else:
            zer=zer+1
    ans=on*zer
    o=0
    z=0
    maxo=0
    maxz=0
    for j in range(n):
        cnt=0
        if s[j]=="1":
            o=o+1
            maxo=max(maxo,o)
        else:
            o=0
    for j in range(n):
        if s[j]=="0":
            z=z+1
            maxz=max(maxz,z)
        else:
            z=0
    maxo=maxo*maxo
    maxz=maxz*maxz
    res=max(ans,maxo,maxz)
    print(res)

