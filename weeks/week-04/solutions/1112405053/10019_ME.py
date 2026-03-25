import sys
for line in sys.stdin:
    try:
        parts = line.split()
        if not parts:
            continue
        a = int(parts[0])
        b = int(parts[1])
        
        print(abs(a - b))
        
    except ValueError: 
        pass
