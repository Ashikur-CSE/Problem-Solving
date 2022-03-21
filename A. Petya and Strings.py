str1=input()
x=str1.upper()
str2=input()
y=str2.upper()
v=0
for i in range(len(x)):
    if ord(x[i])<ord(y[i]):
      v=-1
      break
    elif ord(x[i])==ord(y[i]):
      continue
    else:
        v=1
        break
print(v)   
