x=input()
y=list(x)
y[0]=y[0].upper()
listToStr = ''.join(map(str, y))
print(listToStr)