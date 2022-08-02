for i in range(int(input())):
    p=int(input())
    if p<=1399 :
        print("Division 4")
    elif p>=1600 and p<=1899:
        print("Division 2")
    elif p>=1400 and p<=1599:
        print("Division 3")
    else:
        print("Division 1")