n=int(input())

for i in range(n):
    c1=0
    c2=0
    list1=[]
    s=[]
    x=int(input())
    list1=list(map(int,input().split()))
    s=list(set(list1))
    for i in range(x):
        if s[0]==list1[i]:
            c1+=1
        elif s[1]==list1[i]:
            c2+=1
    if c1>1:
        s.remove(s[0])
    elif c2>1:
        s.remove(s[1])
    for j in range(x):
        if s[0]==list1[j]:
            print(j+1)

          