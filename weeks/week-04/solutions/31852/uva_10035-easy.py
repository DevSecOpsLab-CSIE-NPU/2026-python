"""UVA 10035: 容易記憶版本。"""

import sys


def solve(text: str) -> str:
    answers = []

    for line in text.splitlines():
        if not line.strip():
            continue
        a, b = line.split()
        if a == "0" and b == "0":
            break

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        times = 0

        # 從個位數往前掃，這是最符合直覺也最好記的寫法。
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            if x + y + carry >= 10:
                carry = 1
                times += 1
            else:
                carry = 0
            i -= 1
            j -= 1

        if times == 0:
            answers.append("No carry operation.")
        elif times == 1:
            answers.append("1 carry operation.")
        else:
            # 多於一次時，operation 要加上 s。
            answers.append(f"{times} carry operations.")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))