import sys

def is_jolly_jumper(sequence):
    """
    判斷序列是否為 jolly jumper
    參數：sequence - 整數列表
    返回：True 如果是 jolly jumper，否則 False
    """
    n = len(sequence)
    if n <= 1:
        return True

    # 計算相鄰差的絕對值
    differences = set()
    for i in range(n - 1):
        diff = abs(sequence[i] - sequence[i + 1])
        if diff < 1 or diff >= n or diff in differences:
            return False
        differences.add(diff)

    # 檢查是否包含 1 到 n-1 的所有數字
    return len(differences) == n - 1

def main():
    for line in sys.stdin:
        if line.strip():
            nums = list(map(int, line.split()))
            if len(nums) > 1:
                n = nums[0]
                sequence = nums[1:]
                if len(sequence) == n:
                    if is_jolly_jumper(sequence):
                        print("Jolly")
                    else:
                        print("Not jolly")

if __name__ == "__main__":
    main()