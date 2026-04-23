import sys

lines = sys.stdin.read().splitlines()

if lines:
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)
            
    for i in range(max_len):
        result = ""
        
        for line in reversed(lines):
            if i < len(line):
                result += line[i]
            else:
                result += " "
                
        print(result)