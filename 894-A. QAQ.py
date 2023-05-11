s=input()
c=0
for i in range(len(s)):
    if s[i]=="A":
        a=s[:i].count("Q")*s[i:].count("Q")
        c=c+a
print(c)