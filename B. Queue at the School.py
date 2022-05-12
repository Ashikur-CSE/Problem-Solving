n,x=map(int,input().split())
s=input()
list= list(s)
while(x>0):
    i=0
    while(i<n-1):
        if list[i]=="B" and list[i+1]=="G":
            list[i]="G"
            list[i+1]="B"
            i+=1
        i+=1
    x-=1
listToStr = ''.join(map(str, list))
print(listToStr)
        
      



       