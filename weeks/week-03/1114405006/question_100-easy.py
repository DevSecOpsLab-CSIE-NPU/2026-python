"""UVA 100 的簡單版寫法。

這份版本刻意把流程寫得更直觀：
1. 先把單一數字的 cycle-length 算出來。
2. 再把區間內每個數字都查一遍，找出最大值。

適合背誦的重點只有兩個：
- 奇數：3n + 1
- 偶數：n // 2

這個版本的核心想法是「先往前走，遇到已知答案再往回補」。
因為 Collatz 序列常常會重複碰到相同的數字，所以加上快取後，
同一條路徑上的中間結果可以直接重用，不需要每次都從頭算到尾。
"""

from __future__ import annotations

import sys


class CollatzEasySolver:
    """用快取加上迭代回填，寫成比較好記的版本。

    這個類別只負責兩件事：
    1. 算單一數字的 cycle-length。
    2. 算區間內最大的 cycle-length。

    把責任切小之後，主程式就只要負責讀入與輸出，結構會比較清楚。
    """

    def __init__(self) -> None:
        # 1 的 cycle-length 一定是 1，先放進去當基底。
        # 這樣後面只要走到 1，就知道可以停下來。
        self.cache: dict[int, int] = {1: 1}

    def cycle_length(self, n: int) -> int:
        """計算單一正整數的 cycle-length。

        做法是：
        1. 先一路依照 Collatz 規則往下走，直到碰到已經算過的數字。
        2. 再把這條路徑上的答案從尾端往前回填到快取裡。
        3. 最後直接回傳起點 n 的結果。

        這種寫法比遞迴更容易用紙筆追蹤，也比較適合背誦。
        """

        if n <= 0:
            raise ValueError("n 必須是正整數")

        # 如果這個數字以前算過，就直接回傳，不再重跑整條序列。
        if n in self.cache:
            return self.cache[n]

        # 先一路往下走，記錄走過的數字。
        # path 會存「還沒有答案」的中間點，等一下要反向補回長度。
        path: list[int] = []
        current = n

        # 只要目前的數字還沒有快取，就持續往下一步推進。
        while current not in self.cache:
            path.append(current)
            if current % 2 == 0:
                # 偶數就除以 2，這是 Collatz 的固定規則。
                current //= 2
            else:
                # 奇數就做 3n + 1，這也是 Collatz 的固定規則。
                current = current * 3 + 1

        # 走到已知答案後，開始倒著把長度補回去。
        # 例如 path 若是 [22, 11, 34]，而 current 已經是 17，
        # 那就先知道 17 的長度，再往回算 34、11、22 的長度。
        length = self.cache[current]
        for value in reversed(path):
            length += 1
            self.cache[value] = length

        # 起點 n 的答案已經被寫回 cache，直接回傳即可。
        return self.cache[n]

    def max_cycle_length(self, left: int, right: int) -> int:
        """計算區間內最大的 cycle-length。

        題目允許 i、j 順序顛倒，所以先用 min / max 把區間整理好。
        接著把區間內每個數字都丟進 cycle_length，比出最大值。
        """

        start = min(left, right)
        end = max(left, right)
        # 區間是包含頭尾的，所以 range 要寫到 end + 1。
        return max(self.cycle_length(number) for number in range(start, end + 1))


def solve_text(text: str) -> str:
    """把多行輸入轉成題目要求的輸出格式。

    題目的輸入是一列一組 i j，因此這裡的工作就是：
    1. 逐列讀入。
    2. 忽略空白列。
    3. 算出該列答案後，組回 `i j ans` 的格式。
    """

    solver = CollatzEasySolver()
    output_lines: list[str] = []

    for raw_line in text.splitlines():
        raw_line = raw_line.strip()
        if not raw_line:
            # 空白列直接跳過，避免 split() 出錯。
            continue

        # 每列都只有兩個整數，分別代表區間左右端點。
        left_str, right_str = raw_line.split()
        left = int(left_str)
        right = int(right_str)
        best = solver.max_cycle_length(left, right)

        # 輸出格式要保留原始的 i、j，再接上最大 cycle-length。
        output_lines.append(f"{left} {right} {best}")

    return "\n".join(output_lines)


def main() -> None:
    """命令列入口。

    這裡只做兩件事：
    1. 從標準輸入讀完全部內容。
    2. 有內容就交給 solve_text，然後印出結果。
    """

    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve_text(input_text))


if __name__ == "__main__":
    main()