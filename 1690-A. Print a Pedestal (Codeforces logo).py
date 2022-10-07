for i in range(int(input())):
    n=int(input())
    h2=(n+1)//3
    h1=(n+5)//3
    h3=(n//3)-1
    print(h2,h1,h3)
    # h2=(n//3)
    # h1=(h2+1)
    # h3=(h2-1)
    # if h2==h3:
    #     h3=(h3-1)
    #     h1=h1+1
    # if (h1+h2+h3!=n):
    #     h2=h2+1
    