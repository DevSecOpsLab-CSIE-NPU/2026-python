"""題目 948 附件描述版本：容易記憶寫法。"""

import sys


def solve(text: str) -> str:
    data = text.split()
    if not data:
        return ""

    t = int(data[0])
    pos = 1
    answers = []

    for case_id in range(t):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2

        checks = []
        for _ in range(k):
            p = int(data[pos])
            pos += 1
            left = list(map(int, data[pos : pos + p]))
            pos += p
            right = list(map(int, data[pos : pos + p]))
            pos += p
            mark = data[pos]
            pos += 1
            checks.append((left, right, mark))

        good = []
        for coin in range(1, n + 1):
            for heavy in (True, False):
                # heavy=True 代表假幣比較重，False 代表比較輕。
                ok = True
                for left, right, mark in checks:
                    in_left = coin in left
                    in_right = coin in right

                    if not in_left and not in_right:
                        if mark != "=":
                            ok = False
                            break
                    else:
                        if mark == "=":
                            ok = False
                            break
                        if in_left:
                            need = ">" if heavy else "<"
                        else:
                            need = "<" if heavy else ">"
                        if mark != need:
                            ok = False
                            break

                if ok:
                    # 這枚硬幣只要有一種情況成立，就不用再測第二種。
                    good.append(coin)
                    break

        if len(good) == 1:
            answers.append(str(good[0]))
        else:
            answers.append("0")

        if case_id != t - 1:
            answers.append("")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))