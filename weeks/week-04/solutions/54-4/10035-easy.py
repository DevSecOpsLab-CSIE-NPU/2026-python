import sys

def count_carry_operations_simple(a, b):
    """
    簡易版本：計算進位次數
    將數字轉為字符串處理
    """
    str_a = str(a)
    str_b = str(b)

    # 補齊長度
    max_len = max(len(str_a), len(str_b))
    str_a = str_a.zfill(max_len)
    str_b = str_b.zfill(max_len)

    carry_count = 0
    carry = 0

    for i in range(max_len - 1, -1, -1):
        digit_a = int(str_a[i])
        digit_b = int(str_b[i])

        total = digit_a + digit_b + carry

        if total >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0

    return carry_count

def main():
    for line in sys.stdin:
        if line.strip():
            nums = list(map(int, line.split()))
            if len(nums) == 2:
                a, b = nums
                if a == 0 and b == 0:
                    break
                carry_count = count_carry_operations_simple(a, b)
                if carry_count == 0:
                    print("No carry operation.")
                elif carry_count == 1:
                    print("1 carry operation.")
                else:
                    print(f"{carry_count} carry operations.")

if __name__ == "__main__":
    main()