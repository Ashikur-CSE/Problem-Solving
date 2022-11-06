# for i in range(int(input())):
#     def sum(a,b,c):
#         x=a+b
#         y=a+c
#         z=b+c
#         if x==a or x==b or x==c or y==a or y==b or y==c or z==a or z==b or z==c:
#             return "YES"
#         else:
#             return "NO"


#     a,b,c = map(int,input().split())
#     var = res=sum(a,b,c)
#     print(res)
for i in range(int(input())):
    a,b,c =list(sorted(map(int,input().split())))
    if a+b==c:
        print("YES")
    else:
        print("NO")




