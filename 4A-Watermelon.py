w=int(input())
if w>2:
    if w%2==0:
        r=w/2
        if r%2==0 or (r+1)%2==0:
            print("Yes\n")
        else:
            print("No\n")
    else:
        print("No\n")
else:
    print("No\n")