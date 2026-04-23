import sys

text = sys.stdin.read().upper()

results = []

for i in range(65, 91):
    char = chr(i)
    count = text.count(char)
    
    if count > 0:
        results.append([-count, char])
        
results.sort()

for item in results:
    count = -item[0]
    char = item[1]
    print(f"{char} {count}")