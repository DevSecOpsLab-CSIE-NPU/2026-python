import sys

opening = True
result = ""

for line in sys.stdin:
    for char in line:
        if char == '"':
            result += "``" if opening else "''"
            opening = not opening
        else:
            result += char

sys.stdout.write(result)
