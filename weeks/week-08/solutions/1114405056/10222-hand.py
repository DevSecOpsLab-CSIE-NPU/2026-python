KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
POS = {c: i for i, c in enumerate(KEYBOARD)}

while True:
    try:
        line = input()
    except EOFError:
        break

    result = []
    for c in line:
        if c == ' ':
            result.append(' ')
        elif c in POS:
            p = POS[c]
            if p >= 3:
                result.append(KEYBOARD[p - 3])
        else:
            result.append(c)
    print(''.join(result))
