# 10019.py
# UVA 10019：Funny Encryption Method
# 功能：計算十進位轉二進位的 1 個數 (b1) 以及將其視為十六進位轉二進位的 1 個數 (b2)

import sys

class EncryptionAnalyzer:
    @staticmethod
    def count_set_bits(n: int) -> int:
        """計算整數 n 在二進位下的 1 的個數。"""
        return bin(n).count('1')

    def analyze(self, m_str: str) -> tuple:
        # b1: 正常的十進位轉二進位
        n_dec = int(m_str)
        b1 = self.count_set_bits(n_dec)

        # b2: 視為十六進位轉二進位
        n_hex = int(m_str, 16)
        b2 = self.count_set_bits(n_hex)

        return b1, b2

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_cases = int(input_data[0])
    analyzer = EncryptionAnalyzer()

    for i in range(1, n_cases + 1):
        m_str = input_data[i]
        b1, b2 = analyzer.analyze(m_str)
        print(f"{b1} {b2}")

if __name__ == "__main__":
    main()
