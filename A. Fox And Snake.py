a,b=map(int,input().split())
i=1
for i in range(1,a+1):
    if i==1:
        print("#"*b)
    elif i>1 and i%4==2:
        z=i
        print("."* (b-1) +"#")
    elif i%4==0:
        print("#" + "." * (b-1))
    elif i>1 and i%2!=0:
        print("#"*b)