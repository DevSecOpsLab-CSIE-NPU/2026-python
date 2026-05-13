import sys
data = sys.stdin.read().split()
n = int(data[0])
index = 1 
for _ in range(n):
    S = int(data[index])    
    D = int(data[index + 1])  
    index += 2 
    a = (S + D) // 2 
    b = (S - D) // 2  
    if a >= 0 and b >= 0 and (S + D) % 2 == 0:
        print(a, b)  
    else:
        print("impossible") 