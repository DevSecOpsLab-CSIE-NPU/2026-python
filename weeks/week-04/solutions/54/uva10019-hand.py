while True:
    try:
        a, b = map(int, input().split())
        if a > b:
            print(a - b)
        else:
            print(b - a)
    except EOFError:
        break
