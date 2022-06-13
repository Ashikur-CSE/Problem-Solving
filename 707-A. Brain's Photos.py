n,m=map(int,input().split())
s=''.join(input() for i in range(n))
if s.count('C') + s.count('M') + s.count('Y') > 0:
	print ('#Color')
else:
	print ('#Black&White')
