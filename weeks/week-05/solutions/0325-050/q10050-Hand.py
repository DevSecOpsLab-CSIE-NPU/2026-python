import sys

data = [int(x) for x in sys.stdin.read().split()]

if data:
    test_cases = data[0]
    idx = 1
    
    for _ in range(test_cases):
        N = data[idx]
        P = data[idx + 1]
        idx += 2
        
        parties = data[idx : idx + P]
        idx += P
        
        hartals = set()
        
        for h in parties:
            for day in range(h, N + 1, h):
                if day % 7 != 6 and day % 7 != 0:
                    hartals.add(day)
                    
        print(len(hartals))