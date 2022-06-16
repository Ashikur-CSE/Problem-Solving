n = int(input())
for i in range(n):
    k = input()
    d = len(k)
    total = 9*(d-1) + int(k)//int(d*"1")
    print(total)