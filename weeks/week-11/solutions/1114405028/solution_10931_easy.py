"""UVA 10931 — Parity 簡單版本"""


def parity_simple(num):
    """最簡單的解法"""
    binary = bin(num)[2:]
    ones = binary.count("1")
    return f"The parity of {binary} is {ones} (mod 2)."


if __name__ == "__main__":
    print(parity_simple(1))   # The parity of 1 is 1 (mod 2).
    print(parity_simple(2))   # The parity of 10 is 1 (mod 2).
    print(parity_simple(10))  # The parity of 1010 is 2 (mod 2).
    print(parity_simple(21))  # The parity of 10101 is 3 (mod 2).
