import sys
for line in sys.stdin:
    num = line.strip()
    if num == '0':
        break
    degree = 0
    while len(num) > 1:
        num = str(sum(int(d) for d in num))
        degree += 1
    if num == '9':
        print(f"9-degree of {line.strip()} is {degree}.")
    else:
        print(f"{line.strip()} is not a multiple of 9.")