"""
UVA 10056 - What is the Probability ?
測試程式版本

用途說明：
這份程式主要用來做本地測試。
程式將核心計算邏輯獨立成函式，
方便檢查答案是否正確，也方便後續維護與除錯。
"""


def calculate_win_probability(player_count, success_probability, target_player):
    """
    計算第 target_player 位玩家最終獲勝的機率。

    參數：
        player_count (int)：玩家總人數 n
        success_probability (float)：每位玩家在自己回合成功的機率 p
        target_player (int)：欲求最終獲勝機率的玩家編號 i

    回傳：
        float：第 target_player 位玩家最終獲勝的機率

    解題觀念：
        第 i 位玩家在某一輪獲勝的條件為：
        1. 前面 i - 1 位玩家皆失敗
        2. 第 i 位玩家成功

        第一輪直接獲勝機率為：
        (1 - p)^(i - 1) * p

        若整輪 n 位玩家都失敗，則會重新開始下一輪，
        其機率為：
        (1 - p)^n

        因此可形成無窮等比級數，整理後公式為：
        ((1 - p)^(i - 1) * p) / (1 - (1 - p)^n)

        若 p = 0，則不可能有人成功，答案為 0。
    """

    # 若成功機率為 0，任何玩家都不可能獲勝
    if success_probability == 0:
        return 0.0

    # q 代表失敗機率
    failure_probability = 1 - success_probability

    # 依公式計算最終獲勝機率
    probability = (
        (failure_probability ** (target_player - 1)) * success_probability
    ) / (1 - (failure_probability ** player_count))

    return probability


def solve():
    """
    依照 UVA 題目的輸入格式讀取資料並輸出答案。
    """

    # 讀入測試資料組數
    test_case_count = int(input().strip())

    # 逐組處理
    for _ in range(test_case_count):
        # 讀入一組資料：n p i
        player_count, success_probability, target_player = input().split()

        # 轉換型態
        player_count = int(player_count)
        success_probability = float(success_probability)
        target_player = int(target_player)

        # 計算答案
        answer = calculate_win_probability(
            player_count, success_probability, target_player
        )

        # 依題目要求輸出到小數點後四位
        print(f"{answer:.4f}")


# 程式進入點
if __name__ == "__main__":
    solve()