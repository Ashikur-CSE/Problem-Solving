for i in range (int(input())):
    l1=[]
    n=int(input())
    if n<500:
        for i in range(1, n+1):
            x=(2 * i - 1)
            l1.append(x)
            s = [str(i) for i in l1] 
            result = str(" ".join(s)) 
        print(result)
    elif n>500:
        for i in range(1, 501):
            x=(2 * i - 1)
            l1.append(x)
            x=(2*l1)
            s = [str(i) for i in x[:n]] 
            result = str(" ".join(s)) 
        print(result)
# other solution
# for _ in range(int(input())):
#   print('1 '*int(input()))