def count_carry(a: int, b: int) -> int:
    # carry 用來記錄「前一位有沒有進位」
    # 若前一位有進位，carry = 1，否則為 0
    carry = 0

    # count 用來統計總共發生幾次進位
    count = 0

    # 只要 a 或 b 還有數字，就持續逐位相加
    while a > 0 or b > 0:
        # 先取出個位數，再加上前一位帶來的進位
        digit_sum = a % 10 + b % 10 + carry

        # 如果這一位的和大於等於 10，代表這一位有進位
        if digit_sum >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        # 去掉目前已經處理完的個位數，往十位數繼續處理
        a //= 10
        b //= 10

    # 回傳總進位次數
    return count


def solve(data: str) -> str:
    # 用來儲存每一組測資的輸出結果
    answers = []

    # 逐行讀取輸入資料
    for line in data.strip().splitlines():
        # 每一列有兩個整數
        a, b = map(int, line.split())

        # 若讀到 0 0，代表輸入結束
        if a == 0 and b == 0:
            break

        # 計算這兩個數相加時的進位次數
        carry_count = count_carry(a, b)

        # 依照題目要求輸出對應文字
        if carry_count == 0:
            answers.append("No carry operation.")
        elif carry_count == 1:
            answers.append("1 carry operation.")
        else:
            answers.append(f"{carry_count} carry operations.")

    # 每組答案用換行連接
    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    # 從標準輸入讀取整份資料，再交給 solve 處理
    input_data = sys.stdin.read()
    print(solve(input_data))