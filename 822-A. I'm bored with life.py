import math
a,b=map(int,input().split())
if a>b:
    print(math.factorial(b))
else:
    print(math.factorial(a))


# if x>y:
#     temp=y
# else:
#     temp=x
# for i in range(1,temp+1):
#     if(a%i==0)and(b%i==0):
#         gcd.append(i)
# print(gcd[-1])


