def is_jolly_jumper(n, seq):
    if n == 1:
        return True
    
    differences = set()
    for i in range(n - 1):
        diff = abs(seq[i] - seq[i + 1])
        if diff == 0 or diff > n - 1:
            return False
        if diff in differences:
            return False
        differences.add(diff)
    
    return len(differences) == n - 1

while True:
    data = list(map(int, input().split()))
    n = data[0]
    if n == 0:
        break
    seq = data[1:n+1]
    
    if is_jolly_jumper(n, seq):
        print("Jolly")
    else:
        print("Not jolly")
