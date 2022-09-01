# for i in range(int(input())):
#     s=list(input())
#     l=len(s)
#     s2=input()
#     n=(l-3)
#     if l>3:
#         for i in range(n):
#             s.remove(s[0])
#         if s2 in s and s[1]!=s2 :
#             print("YES")
#         elif s[0]==s2 and s[1]==s2 and s[2]==s2:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         if s2 in s and s[1]!=s2:
#             print("YES")
#         elif s[0]==s2 and s[1]==s2 and s[2]==s2:
#             print("YES")
#         else:
#             print("NO")

s = input()
print(s[::2] )
    