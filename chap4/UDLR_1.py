SIZE = int(input())

N = 1
M = 1

ways = list(map(str, input().split()))

for way in ways:
    if((way == "R") & (M < SIZE)):
        M += 1
        print(N, M)  
    elif((way == 'L') & (M > 1)):
        M -= 1
        print(N, M)  
    elif((way == 'U') & (N > 1)):
        N -= 1
        print(N, M)  
    elif((way == 'D') & (N < SIZE)):
        N += 1
        print(N, M)  

print(N, M)        
