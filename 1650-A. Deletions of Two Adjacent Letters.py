for i in range(int(input())):
    s = input()
    n=input()
    l1=s[::2]
    if n in l1:
        print("Yes")
    else:
        print("NO")
    