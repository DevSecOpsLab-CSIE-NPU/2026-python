import sys

def is_jolly_jumper_simple(sequence):
    """
    簡易版本：判斷 jolly jumper
    使用列表檢查差值
    """
    n = len(sequence)
    if n <= 1:
        return True

    required_diffs = set(range(1, n))
    found_diffs = set()

    for i in range(n - 1):
        diff = abs(sequence[i] - sequence[i + 1])
        if diff in found_diffs or diff not in required_diffs:
            return False
        found_diffs.add(diff)

    return len(found_diffs) == n - 1

def main():
    for line in sys.stdin:
        if line.strip():
            nums = list(map(int, line.split()))
            if len(nums) > 1:
                n = nums[0]
                sequence = nums[1:]
                if len(sequence) == n:
                    if is_jolly_jumper_simple(sequence):
                        print("Jolly")
                    else:
                        print("Not jolly")

if __name__ == "__main__":
    main()