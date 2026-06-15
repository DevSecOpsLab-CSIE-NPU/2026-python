# 10038.py
# UVA 10038：Jolly Jumpers
# 功能：判斷一個數列是否為 Jolly Jumper (相鄰差值包含 1 到 n-1)

import sys

class JollyJumper:
    @staticmethod
    def is_jolly(nums: list) -> bool:
        n = nums[0]
        if n == 1:
            return True

        elements = nums[1:]
        diffs = set()

        for i in range(len(elements) - 1):
            diff = abs(elements[i] - elements[i+1])
            if 1 <= diff <= n - 1:
                diffs.add(diff)

        return len(diffs) == n - 1

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        data = list(map(int, line.split()))
        if not data:
            continue

        if JollyJumper.is_jolly(data):
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    main()
