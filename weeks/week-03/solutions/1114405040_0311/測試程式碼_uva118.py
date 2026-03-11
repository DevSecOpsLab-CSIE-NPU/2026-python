"""
測試程式碼 - UVA 118 Martian Robots (ZeroJudge c082)

【題目說明】
  機器人在矩形土地上依指令移動（L 左轉、R 右轉、F 前進）。
  掉出邊界的機器人會留下「標記」，有標記的格子之後的機器人
  若遇到會使其掉落的 F 指令，會直接忽略該指令。

【解法說明】
  - 方向順序 ['N','E','S','W']，左轉 -1、右轉 +1（mod 4）
  - 用集合 scents 記錄掉落點
  - 機器人掉落時輸出最後位置 + "LOST"
"""

# ── 解法核心 ────────────────────────────────────────────
# 方向陣列（順時針：N→E→S→W）
DIRECTIONS = ['N', 'E', 'S', 'W']

# 各方向的 x, y 位移
DX = {'N': 0, 'E': 1, 'S':  0, 'W': -1}
DY = {'N': 1, 'E': 0, 'S': -1, 'W':  0}


def simulate(max_x, max_y, robots):
    """
    模擬所有機器人的移動。

    參數：
      max_x, max_y : 矩形土地右上角座標
      robots       : list of (x, y, facing, commands)

    回傳：
      list of 輸出字串（每個機器人一行）
    """
    scents = set()   # 記錄曾有機器人掉落的格子位置
    results = []

    for (x, y, facing, commands) in robots:
        lost = False   # 標記此機器人是否已掉落

        for cmd in commands:
            if cmd == 'L':
                # 左轉：方向索引 -1（mod 4 確保循環）
                facing = DIRECTIONS[(DIRECTIONS.index(facing) - 1) % 4]
            elif cmd == 'R':
                # 右轉：方向索引 +1
                facing = DIRECTIONS[(DIRECTIONS.index(facing) + 1) % 4]
            elif cmd == 'F':
                new_x = x + DX[facing]
                new_y = y + DY[facing]

                if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                    # 即將越界
                    if (x, y) not in scents:
                        # 無標記：掉落，留下標記，停止後續指令
                        scents.add((x, y))
                        lost = True
                        break
                    # 有標記：忽略這個 F 指令，機器人原地不動
                else:
                    # 正常前進
                    x, y = new_x, new_y

        if lost:
            results.append(f"{x} {y} {facing} LOST")
        else:
            results.append(f"{x} {y} {facing}")

    return results


# ── 測試函式 ────────────────────────────────────────────
def run_tests():
    """執行所有測試案例，比對實際輸出與預期輸出。"""

    # 測試案例格式：(max_x, max_y, [(x, y, facing, commands), ...], [預期輸出, ...])
    test_cases = [
        (
            # 測試案例 1：UVA 118 原題範例
            5, 3,
            [
                (1, 1, 'E', 'RFRFRFRF'),
                (3, 2, 'N', 'FRRFLLFFRRFLL'),
                (0, 3, 'W', 'LLFFFLFLFL'),
            ],
            [
                "1 1 E",
                "3 3 N LOST",
                "2 3 S",
            ]
        ),
        (
            # 測試案例 2：機器人只轉向不移動
            5, 5,
            [
                (2, 2, 'N', 'LLLL'),   # 轉四次等於沒轉
            ],
            [
                "2 2 N",
            ]
        ),
        (
            # 測試案例 3：標記保護後續機器人
            2, 2,
            [
                (2, 2, 'N', 'F'),    # 第一個機器人往北掉落，留下標記 (2,2)
                (2, 2, 'N', 'F'),    # 第二個機器人在有標記的 (2,2)，F 被忽略
            ],
            [
                "2 2 N LOST",
                "2 2 N",
            ]
        ),
        (
            # 測試案例 4：往南掉出邊界
            3, 3,
            [
                (0, 0, 'S', 'F'),
            ],
            [
                "0 0 S LOST",
            ]
        ),
    ]

    passed = 0
    failed = 0

    print("=" * 55)
    print("UVA 118 測試結果")
    print("=" * 55)

    for idx, (max_x, max_y, robots, expected_list) in enumerate(test_cases, 1):
        results = simulate(max_x, max_y, robots)

        # 每個測試案例可能有多個機器人，逐一比對
        case_pass = True
        for r, e in zip(results, expected_list):
            if r != e:
                case_pass = False
                break

        if case_pass:
            passed += 1
            print(f"[PASS]  測試案例 {idx}")
        else:
            failed += 1
            print(f"[FAIL]  測試案例 {idx}")
            for r, e in zip(results, expected_list):
                flag = "✓" if r == e else "✗"
                print(f"        {flag} 輸出: '{r}'  預期: '{e}'")

    print("-" * 55)
    print(f"共 {passed + failed} 組，通過 {passed} 組，失敗 {failed} 組")


# ── 主程式 ──────────────────────────────────────────────
if __name__ == "__main__":
    run_tests()
