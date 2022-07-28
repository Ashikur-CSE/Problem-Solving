for i in range (int(input())):
    s=[int(x) for x in input()]
    l2=[]
    l2.append(s[0])
    l2.append(s[1])
    l2.append(s[2])
    if (sum(s)-sum(l2))==sum(l2):
        print("YES")
    else:
        print("NO")

    

