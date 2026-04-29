# UVA 10252 - Common Permutation
import sys
from collections import Counter


def solve_standard():
    """
    Standard: 使用 sys.stdin.read 和 collections.Counter 來高效統計字母。
    """
    lines = sys.stdin.read().splitlines()
    for i in range(0, len(lines) - 1, 2):
        a = lines[i]
        b = lines[i + 1]

        ca = Counter(a)
        cb = Counter(b)

        common = ca & cb
        res = []
        for char in sorted(common.keys()):
            res.append(char * common[char])

        print("".join(res))


def solve_easy():
    """
    Easy: 使用 string 的 count 方法，內建字母表，直觀易懂。
    """
    while True:
        try:
            a = input()
            b = input()
        except EOFError:
            break

        result = ""
        for char in "abcdefghijklmnopqrstuvwxyz":
            count_a = a.count(char)
            count_b = b.count(char)
            result += char * min(count_a, count_b)

        print(result)


def solve_manual():
    """
    Manual: 手寫陣列計數 (ASCII 位移)，不使用任何高階模組，方便考試默寫。
    """
    while True:
        try:
            a = input()
            b = input()
        except EOFError:
            break

        counts_a = [0] * 26
        counts_b = [0] * 26

        for char in a:
            if "a" <= char <= "z":
                idx = ord(char) - ord("a")
                counts_a[idx] += 1

        for char in b:
            if "a" <= char <= "z":
                idx = ord(char) - ord("a")
                counts_b[idx] += 1

        result = ""
        for i in range(26):
            common_count = counts_a[i] if counts_a[i] < counts_b[i] else counts_b[i]
            for _ in range(common_count):
                result += chr(i + ord("a"))

        print(result)


if __name__ == "__main__":
    solve_standard()
