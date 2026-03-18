from __future__ import annotations


def count_ones(number: int) -> int:
    return bin(number).count("1")


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    test_case_count = int(lines[0])
    answers: list[str] = []

    for number_text in lines[1 : 1 + test_case_count]:
        # 先把輸入當成十進位整數解讀。
        decimal_value = int(number_text)

        # 再把同一串文字當成十六進位整數解讀。
        hex_value = int(number_text, 16)
        answers.append(f"{count_ones(decimal_value)} {count_ones(hex_value)}")

    return "\n".join(answers)


def main() -> None:
    import sys

    # 分別計算十進位與十六進位解讀後的二進位 1 的個數。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()