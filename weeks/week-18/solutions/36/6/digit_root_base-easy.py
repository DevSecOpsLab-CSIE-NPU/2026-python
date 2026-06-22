"""
簡易版：進位數字根（易懂版）

說明：此檔案提供一個容易理解的實作，步驟直觀，適合初學者閱讀。

功能：
- `digit_root_base_easy(value, base)` 計算 value 在 base 下的數字根
- 支援 base 範圍同主程式

使用方式（命令列測試）：
    python digit_root_base-easy.py 7 < input.txt

"""

ALLOWED_BASES = {2,3,5,6,7,8,9,10,11,13,16}


def digit_root_base_easy(value: int, base: int) -> int:
    """直覺版實作說明：

    1. 如果 value 為 0，回傳 0
    2. 將 value 用 while 轉為 base 的各位，並加總
    3. 若加總結果仍 >= base，重複步驟 2
    4. 最後回傳結果（十進位數字）
    """
    if base not in ALLOWED_BASES:
        raise ValueError("base not supported")
    if value == 0:
        return 0
    current = value

    while current >= base:
        total = 0
        n = current
        # 逐位取餘相加
        while n > 0:
            total += n % base
            n //= base
        current = total
    return current

    if __name__ == '__main__':
        import sys
        if len(sys.argv) < 2:
            print("Usage: python digit_root_base-easy.py <base>", file=sys.stderr)
            sys.exit(2)
        base = int(sys.argv[1])
        if base not in ALLOWED_BASES:
            print(f"Error: base must be one of {sorted(ALLOWED_BASES)}", file=sys.stderr)
            sys.exit(2)
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            value = int(line)
            print(digit_root_base_easy(value, base))