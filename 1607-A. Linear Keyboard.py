for i in range(int(input())):
    l1=[i for i in input()]
    s=[i for i in input()]
    c=0
    a=0
    n = []
    for i in s:
        x=l1.index(i)+1
        n.append(x)
    for i in range(1,len(n)):
        a+=abs(n[i]-n[i-1])
    print(a)