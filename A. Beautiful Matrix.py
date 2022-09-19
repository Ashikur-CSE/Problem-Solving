mat=[list(map(int,input().split())) for i in range(5)]

for j in range(len(mat)):
    for i in range(len(mat)):
        if mat[j][i]==1:
            
            print(abs(2 - j) + abs(2 - i))
