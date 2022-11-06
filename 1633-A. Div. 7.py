# for i in range(int(input())):
#     n=input()
#     l1=list(n)
#     l=len(n)
#     for i in range(0,10):
#         l1[-1]=str(i)
#         listToStr = ''.join([str(elem) for elem in l1])
#         x=int(listToStr)
#         if x%7==0:
#             print(x)
#             break
for i in range(int(input())):
  n=int(input())
  a=n%7
  b=n%10
  if b<a:
      print(n-a+7)
  else:
      print(n-a)
