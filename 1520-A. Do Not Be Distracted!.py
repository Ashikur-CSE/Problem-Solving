t=int(input())
for x in range(t):
  l = int(input())
  n = input()
  
  for i in range(1, len(n)):
   
    if(n[i] in n[:i] and n[i] != n[i-1]):
      print("NO")
      break
  else:
    print('YES')