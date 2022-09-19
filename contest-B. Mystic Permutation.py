

for i in range(int(input())):
    n=int(input())
    list1=list(map(str,input().split()))
    if len(list1)==1:
        print(-1)
    else:
        for i in range(1,len(list1)):
            list1[i-1],list1[i] = list1[i], list1[i-1]
        res =(" ".join(map(str, list1)))
        print(res)