n1=input()
n2=input()
for i in range(len(n1)):
    if n1[i]==n2[i]:
        print(0,end='')
    else:
        print(1,end='')
