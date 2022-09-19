n=int(input())
while True:
    n=n+1
    if len(set(str(n)))==len(str(n)):
        break
print(n)
