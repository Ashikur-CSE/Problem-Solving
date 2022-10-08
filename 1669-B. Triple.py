for i in range(int(input())):
  n=int(input())
  l=list(map(str,input().split()))
  x=-1
  c=sorted(l)
  for j in range(len(l)-2):
    if c[j]==c[j+1] and c[j]==c[j+2]:
      x=c[j]
      break
  print(x)