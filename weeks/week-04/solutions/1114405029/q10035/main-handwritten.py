while True:
    try:
        line = input().split()
        n1 = line[0]
        n2 = line[1]
        if n1 == '0' and n2 == '0':
            break
        n1 = n1[::-1]
        n2 = n2[::-1]
        carries = 0
        carry = 0
        length = max(len(n1), len(n2))
        for i in range(length):
            d1 = int(n1[i]) if i < len(n1) else 0
            d2 = int(n2[i]) if i < len(n2) else 0
            total = d1 + d2 + carry
            if total >= 10:
                carries += 1
                carry = 1
            else:
                carry = 0
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")
    except EOFError:
        break