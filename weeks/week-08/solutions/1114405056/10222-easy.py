# 瘋狂打字員：鍵盤往右偏移 3 格，把輸入還原成正確文字
# QWERTY 鍵盤由左到右、由上到下排成一列
KEYBOARD = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

# 建立每個字元對應的位置索引
POS = {c: i for i, c in enumerate(KEYBOARD)}

while True:
    try:
        line = input()
    except EOFError:
        break

    result = []
    for c in line:
        if c == ' ':
            result.append(' ')  # 空白不變
        elif c in POS:
            p = POS[c]
            if p >= 3:
                # 往左移 3 格，還原正確的按鍵
                result.append(KEYBOARD[p - 3])
        else:
            result.append(c)  # 其他字元不變
    print(''.join(result))
