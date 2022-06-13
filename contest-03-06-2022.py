for i in range(int(input())):
    n=int (input())
    i=1
    while(True):
        if (n & i)>0 and (n ^ i)>0:
            break   
        i+=1
    print(i)

