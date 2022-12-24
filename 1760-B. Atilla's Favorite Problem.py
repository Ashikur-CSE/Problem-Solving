for i in range(int(input())):
    import string
    n=int(input())
    s1=input()
    l1=[]

    for i in range(n):
        a=s1[i]
        x=string.ascii_lowercase.index(s1[i])
        l1.append(x+1)
    print(max(l1))

