"""
UVA 10922 — 2 the 9s 解決方案
判斷數字是否為 9 的倍數，並計算 9 的深度。
"""


def calculate_nine_degree(num_str):
    """計算 9 的深度並回傳結果與深度。"""
    total = sum(int(ch) for ch in num_str)
    if total % 9 != 0:
        return f"{num_str} is not a multiple of 9.", 0

    depth = 1
    while total > 9:
        total = sum(int(ch) for ch in str(total))
        depth += 1

    return f"9-degree of {num_str} is {depth}.", depth


def main():
    while True:
        line = input().strip()
        if line == "0":
            break

        output, _ = calculate_nine_degree(line)
        print(output)


if __name__ == "__main__":
    main()
