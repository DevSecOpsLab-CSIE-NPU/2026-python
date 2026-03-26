try:
    while True:
        a, b = map(int, input().split())
        print(abs(a - b))
except EOFError:
    pass