for i in range(int(input())): 
    n = int(input()) 
    c=0 
    s1=input() 
    s2=input() 
    for j in range(n): 
        if (s1[j]=="R"): 
            if (s2[j]=="R"): 
                continue 
            else: 
                c=c+1 
                break 
        elif(s2[j]=="R"): 
            c=c+1 
            break 
        else: 
            continue 
    if(c==1): 
        print("NO") 
    else: 
        print("YES")