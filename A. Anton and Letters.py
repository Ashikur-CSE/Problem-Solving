a = list(map(str, input()))
set=set()
for i in range(len(a)):
    if a[i]>="a" and a[i]<="z":
        set.add(a[i])
print(len(set))