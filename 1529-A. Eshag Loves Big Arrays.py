for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    x=li.count(min(li))
    print(n-x)


# 2nd solution//////////////////////////////////////////
# for i in range(int(input())):
#     n=int(input())
#     l1=list(map(int,input().split()))
#     lf=[]
#     l3=sorted(l1)
#     avg=(l3[0]+l3[1])//2
#     l2=set(l1)
#     for j in range(n):
#         if l3[j]<=avg:
#             lf.append(l3[j])
#         else:
#             break
#     print(abs(n-len(lf)))
























    # l2=set(l1)
    # if len(l2)==1:
    #     print(0)
    # else:
    #     res=n-(len(l2))
    #     print(res)
    # print(len(l2))