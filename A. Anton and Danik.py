n=int(input())
s=input()
x=list(s)
count1=0
count2=0
for i in x:
    if i=="A":
        count1=count1+1
    else:
        count2=count2+1
if count1>count2:
    print("Anton")
elif count2>count1:
    print("Danik")
else:
    print("Friendship")