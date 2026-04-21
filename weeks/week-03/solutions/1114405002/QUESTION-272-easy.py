import sys


def main() -> None:
    # 用一個列表包住狀態，方便在函式裡修改。
    quote_state = [True]
    converted_text = []

    for line in sys.stdin:
        for character in line:
            if character == '"':
                # 第一個雙引號變成 ``，第二個變成 ''，之後交替出現。
                if quote_state[0]:
                    converted_text.append('``')
                else:
                    converted_text.append("''")

                # 每看到一個雙引號，狀態就反轉一次。
                quote_state[0] = not quote_state[0]
            else:
                # 其他字元原樣保留。
                converted_text.append(character)

    sys.stdout.write(''.join(converted_text))


if __name__ == '__main__':
    main()