n = int(input())  

while True:
    print(n)          
    if n == 1:        
        break
    if n % 2 == 1:    
        n = 3 * n + 1 
    else:             
        n = n // 2