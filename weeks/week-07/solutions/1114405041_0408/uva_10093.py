import sys


def char_to_value(char: str) -> int:
    """把題目中的單一字元轉成對應數值。"""
    if "0" <= char <= "9":
        return ord(char) - ord("0")
    if "A" <= char <= "Z":
        return ord(char) - ord("A") + 10
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 36
    raise ValueError(f"不支援的字元: {char}")


def find_smallest_base(token: str) -> str:
    """
    UVA 10093 的關鍵性質：
    一個數在 base b 下對 (b - 1) 取模，結果會等於各位數字總和對 (b - 1) 取模。
    因此只要從最小可能進位制一路檢查到 62 即可。
    """
    digit_values = [char_to_value(char) for char in token]
    minimum_base = max(2, max(digit_values) + 1)
    digit_sum = sum(digit_values)

    for base in range(minimum_base, 63):
        if digit_sum % (base - 1) == 0:
            return str(base)

    return "such number is impossible!"


def solve(data: str) -> str:
    outputs = []

    for line in data.splitlines():
        token = line.strip()
        if not token:
            continue
        outputs.append(find_smallest_base(token))

    return "\n".join(outputs)


def main() -> None:
    # 這題同樣是多筆輸入直到 EOF。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()