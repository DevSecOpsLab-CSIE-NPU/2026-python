# UVA 10226 - Hardwood Species
# 詳細註解版（繁體中文）

import sys
from collections import Counter


def solve() -> None:
    # 一次讀入整份輸入，保留換行以便精準處理「空白行分段」格式
    raw = sys.stdin.read()
    if not raw:
        return

    lines = raw.splitlines()

    # 第一行是測資數量 T
    t = int(lines[0].strip())

    # UVA 10226 的格式通常是：T 後面接一個空白行，再開始第一組資料
    idx = 1
    if idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    out = []

    for case_id in range(t):
        # 讀取一組：直到空白行（或 EOF）為止，每行是一個樹種名稱
        species_counter = Counter()
        total = 0

        while idx < len(lines) and lines[idx].strip() != "":
            name = lines[idx]
            species_counter[name] += 1
            total += 1
            idx += 1

        # 依字典序輸出每個樹種，以及其百分比（小數點後 4 位）
        for name in sorted(species_counter):
            pct = species_counter[name] * 100.0 / total
            out.append(f"{name} {pct:.4f}")

        # 組與組之間要空一行（最後一組不加）
        if case_id != t - 1:
            out.append("")

        # 跳過分隔空白行，準備讀下一組
        while idx < len(lines) and lines[idx].strip() == "":
            idx += 1

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
