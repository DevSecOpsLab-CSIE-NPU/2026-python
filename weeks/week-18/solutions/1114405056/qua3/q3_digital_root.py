"""Question 3: Digital Root in Arbitrary Base.

學號末兩碼為 56，個位數 u = 6，
所以 BASE = 9（使用九進位）。

本題需要計算任意進位的數字根。
輸入為十進位的大整數 N 與進位基底 base。
輸出該數字在該進位底下的數字根。
"""

BASE = 8


def digital_root_base(n, base):
    """計算 N 在指定進位下的數字根。
    
    數字根是將數字的各位數反復相加，
    直到結果只有一個數字的過程。
    
    在進位 base 下，若 n == 0，則返回 0。
    否則使用公式：digital_root = 1 + (n - 1) % (base - 1)
    """
    if n == 0:
        return 0
    return 1 + (n - 1) % (base - 1)


def main():
    import sys

    # 逐行讀取輸入，直到讀到 N = 0 且 Base = 0。
    while True:
        try:
            line = sys.stdin.readline()
            
            # 若為空行，跳過。
            if not line.strip():
                continue
            
            # 解析輸入。
            parts = line.strip().split()
            if len(parts) != 2:
                raise ValueError(f"Expected 2 integers, got {len(parts)}")
            
            n = int(parts[0])
            base = int(parts[1])
            
            # 若 N = 0 且 Base = 0，則結束。
            if n == 0 and base == 0:
                break
            
            # 輸出該數字在 base 進位下的數字根。
            result = digital_root_base(n, base)
            print(result)
            
        except ValueError as e:
            # 捕捉格式錯誤。
            print(f"Error: {e}", file=sys.stderr)
            continue
        except EOFError:
            # 若提早遇到 EOF，則結束。
            break


if __name__ == "__main__":
    main()
