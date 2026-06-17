# R04. 2D 矩陣操作與中心擴張搜尋（UVA 10908）
# 從中心向外擴張，找最大全同字元正方形

# ── 矩陣基本操作 ─────────────────────────────────────────
print("=== 建立矩陣 ===")
grid = [
    "abbbaaaaaa",
    "abbbaaaaaa",
    "abbbaaaaaa",
    "aaaaaaaaaa",
    "aaaaaaaaaa",
    "aaccaaaaaa",
    "aaccaaaaaa",
]
rows = len(grid)
cols = len(grid[0])
print(f"{rows} 行 × {cols} 列")
print(f"grid[1][2] = {grid[1][2]!r}")   # 'b'

# ── 中心擴張：找最大全同字元正方形（邊長為奇數）──────────
def largest_square(grid, r, c):
    """
    以 (r, c) 為中心向外擴張。
    邊長從 1 開始，每次 +2（維持奇數且中心固定）。
    當正方形超出邊界或出現不同字元時停止。
    """
    rows, cols = len(grid), len(grid[0])
    center_char = grid[r][c]
    side = 1        # 當前正方形邊長

    while True:
        half = side // 2
        next_side = side + 2
        next_half = next_side // 2

        # 確認擴張後仍在邊界內
        if (r - next_half < 0 or r + next_half >= rows or
                c - next_half < 0 or c + next_half >= cols):
            break

        # 只需檢查新加入的最外圈
        ok = True
        for dr in range(-next_half, next_half + 1):
            for dc in [-next_half, next_half]:  # 左右兩列
                if grid[r + dr][c + dc] != center_char:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            for dc in range(-next_half, next_half + 1):
                for dr in [-next_half, next_half]:  # 上下兩列
                    if grid[r + dr][c + dc] != center_char:
                        ok = False
                        break
                if not ok:
                    break

        if not ok:
            break
        side = next_side

    return side


# ── 測試（對應 UVA 10908 範例）───────────────────────────
print("\n=== 最大正方形邊長 ===")
queries = [(1, 2), (2, 4), (4, 6), (5, 2)]
expected = [3, 1, 5, 1]

for (r, c), exp in zip(queries, expected):
    result = largest_square(grid, r, c)
    status = "OK" if result == exp else f"FAIL (expected {exp})"
    print(f"中心({r},{c})={grid[r][c]!r}  最大邊長={result}  {status}")
