for i in range(int(input())):
    n,k = map(int, input().split())
    s=input()
    #li = list(s.split(""))
    c=0
    for i in range(k):
        if k*"B" in s:
            c=0
        elif s[i]=="W":
            c=c+1
    print(c)

