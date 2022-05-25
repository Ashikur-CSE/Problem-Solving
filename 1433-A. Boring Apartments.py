t=int(input())
l1=[1,11,111,1111,2,22,222,2222,3,33,333,3333,4,44,444,4444,5,55,555,5555,6,66,666,6666,7,77,777,7777,8,88,888,8888,9,99,999,9999]

for i in range(t):
    x=int(input())
    l2=[]
    for j in range(len(l1)):
        
        if l1[j]==x:
            l2.append(l1[:j+1])
    lts = ''.join(map(str, l2))
    s2 = lts.replace(" ","")
    s3=s2.replace("[","")
    s4=s3.replace("]","")
    s5=s4.replace(",","")
    
    print(len(s5))
