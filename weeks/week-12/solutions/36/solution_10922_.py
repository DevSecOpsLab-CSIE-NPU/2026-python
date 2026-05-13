while True:
    n = input().strip()
    if n == "0":
        break
    depth = 0
    current = sum(int(d) for d in n)

    while current >= 10:
        depth += 1
        current = sum(int(d) for d in str(current))

    if current == 9:
        print(f"9-degree of {n} is {depth + 1}.")
    else:
        print(f"{n} is not a multiple of 9.")
        