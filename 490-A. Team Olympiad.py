n=int(input())
list1=list(map(int,input().split()))
count1=0
count2=0
count3=0
lista=[]
listb=[]
listc=[]
for i in range(n):
    if list1[i]==1:
        count1=count1+1
        lista.append(i)
    elif list1[i]==2:
        count2=count2+1
        listb.append(i)
    elif list1[i]==3:
        count3=count3+1
        listc.append(i)
print(min(count1,count2,count3))
for i in range(min(count1,count2,count3)):
    print(lista[i]+1,listb[i]+1,listc[i]+1)
