# for i in range(int(input())):
#     n=int(input())
#     for i in range(n,1,-1):
#         z=i&(i-1)
#         if z==0:
#             print(i-1)
#             break
for i in range(int(input())):
    n=int(input())
    z=len(bin(n))-3
    print((2**z)-1)


