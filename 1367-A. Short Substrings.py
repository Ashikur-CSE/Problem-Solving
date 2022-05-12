n=int(input())
for i in range(n):
    x=input()
    set2=set(x)
    if len(set2)==1:
            print(((len(x)//2)+1)*(x[0])) 
    if len(x)==2 :
        print(x)
    
    elif len(x)>2 and len(set2)>1 :
        list2=[]
        list1=list(x)
        a=list1[0]
        b=list1[(len(list1)-1)]
        list1.remove(list1[0])
        list1.remove(list1[(len(list1)-1)])
        for j in list1:
            if j not in list2:
                list2.append(j)
        #print(list2)
        #set1=set(list1)
        #s = ''.join(set1)
        print(f"{a}{list2}{b}")
