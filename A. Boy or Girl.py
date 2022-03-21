str=input()
x=''.join(set(str))
c=len(x)
if c%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")