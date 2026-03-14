import sys

inside = False

for line in sys.stdin:
    result = ""
    for ch in line:
        if ch == '"':
            if not inside:
                result += "``"
            else:
                result += "''"
            inside = not inside
        else:
            result += ch
    print(result, end="")