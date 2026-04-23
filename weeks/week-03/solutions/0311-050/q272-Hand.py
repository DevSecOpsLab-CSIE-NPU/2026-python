import sys

is_first = True

for line in sys.stdin:
    result = ""
    
    for c in line:
        if c == '"':
            if is_first:
                result += "``"
            else:
                result += "''"
            is_first = not is_first
        else:
            result += c
            
    print(result, end="")