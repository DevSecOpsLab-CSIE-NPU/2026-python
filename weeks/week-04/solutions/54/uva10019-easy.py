while True:
    try:
        a, b = map(int, input().split())
        diff = a - b
        if diff < 0:
            diff = -diff
        print(diff)
    except EOFError:
        break
