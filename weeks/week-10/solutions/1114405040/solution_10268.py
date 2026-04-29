"""UVA 10268 - Dropping Eggs.

提供 minimum_trials(k, n) 供單元測試呼叫，並支援從標準輸入讀取多筆測資。
"""

from __future__ import annotations

import sys


def minimum_trials(eggs: int, floors: int):
    """回傳最少需要的最糟試驗次數；若超過 63 次則回傳 None。"""

    if floors <= 0:
        return 0
    if eggs <= 0:
        return None

    # reach[i] 代表「在目前試驗次數下，i 顆水球最多可以覆蓋多少樓層」。
    # 這裡使用遞推式：
    # 新的可測樓層數 = 原本可測樓層數 + 少一顆水球時可多測的樓層數 + 1
    reach = [0] * (eggs + 1)
    for trials in range(1, 64):
        # 反向更新，避免同一輪迴圈中覆蓋到尚未使用的舊值。
        for egg in range(eggs, 0, -1):
            reach[egg] = reach[egg] + reach[egg - 1] + 1
        if reach[eggs] >= floors:
            return trials

    return None


def main() -> None:
    results = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # 每筆輸入都是一組 eggs floors；eggs == 0 表示結束。
        eggs, floors = map(int, line.split())
        if eggs == 0:
            break

        trials = minimum_trials(eggs, floors)
        # 題目要求：若超過 63 次，輸出指定字串。
        if trials is None:
            results.append("More than 63 trials needed.")
        else:
            results.append(str(trials))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()