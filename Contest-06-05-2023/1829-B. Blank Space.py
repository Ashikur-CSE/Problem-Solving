for i in range(int(input())):
    n=int(input())
    l1= list(map(int,input().split()))
    max_length = 0 
    current_length = 0 
    for num in l1:
        if num == 0:
                current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
    max_length = max(max_length, current_length)
    print(max_length)