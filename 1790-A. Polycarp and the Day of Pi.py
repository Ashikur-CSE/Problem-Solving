for _ in range(int(input())):
    pi='3141592653589793238462643383279502884197'
    s=input()
    x=pi[:len(s)]
    c=0
    for i in range(len(s)):
        if s[i]==x[i]:
            c=c+1
        else:
            break
    print(c)

