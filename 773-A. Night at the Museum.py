c=97
s=0
for x in input():
	i=abs(c-ord(x))
	s+=min(i,26-i)
	c=ord(x)
print(s)
