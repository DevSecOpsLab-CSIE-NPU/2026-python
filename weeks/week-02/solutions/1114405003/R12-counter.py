"""
R12：Counter 計數器

學習目標：
1. 使用 Counter 快速統計元素次數。
2. 使用 most_common(n) 取得前 n 名。
3. 使用 update 累加新資料。
"""

from collections import Counter


def main():
    print("=== R12 Counter 計數 ===")

    words = ["look", "into", "my", "eyes", "look", "into", "my", "eyes", "eyes"]
    print("[原始 words]", words)

    word_counts = Counter(words)
    print("[例1] 各單字次數 =", word_counts)
    print("[例2] 最常見前 3 名 =", word_counts.most_common(3))

    word_counts.update(["eyes", "eyes", "my"])
    print("[例3] update 後（eyes 與 my 次數增加）=", word_counts)


if __name__ == "__main__":
    main()
