import sys

def count_carry_operations(a, b):
    """
    計算兩個數字相加時的進位次數
    參數：a, b - 兩個正整數
    返回：進位次數
    """
    carry_count = 0
    carry = 0

    while a > 0 or b > 0 or carry > 0:
        digit_a = a % 10
        digit_b = b % 10

        total = digit_a + digit_b + carry

        if total >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0

        a //= 10
        b //= 10

    return carry_count

def main():
    for line in sys.stdin:
        if line.strip():
            nums = list(map(int, line.split()))
            if len(nums) == 2:
                a, b = nums
                if a == 0 and b == 0:
                    break
                carry_count = count_carry_operations(a, b)
                if carry_count == 0:
                    print("No carry operation.")
                elif carry_count == 1:
                    print("1 carry operation.")
                else:
                    print(f"{carry_count} carry operations.")

if __name__ == "__main__":
    main()