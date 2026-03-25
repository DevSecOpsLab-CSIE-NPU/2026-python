from typing import Iterable, List


def is_weekend(day: int) -> bool:
    """第 1 天是星期天；星期五(6)與星期六(0)是週末。"""
    # day % 7 的對應：1=週日, 2=週一, ..., 6=週五, 0=週六
    w = day % 7
    return w == 6 or w == 0


def count_lost_days(n: int, hartals: Iterable[int]) -> int:
    """計算前 n 天因罷會損失的工作天數。"""
    # 用 set 儲存罷會日，避免不同政黨撞在同一天時重複計數。
    lost_days = set()

    for h in hartals:
        # 每個政黨從第 h 天開始，每隔 h 天發生一次罷會。
        d = h
        while d <= n:
            # 週五、週六是假日，不列入損失工作天。
            if not is_weekend(d):
                lost_days.add(d)
            d += h

    return len(lost_days)


def solve(data: str) -> str:
    """解析 UVA 10050 輸入並回傳每組答案。"""
    # 將所有輸入先攤平成整數串列，便於用指標 i 依序讀取。
    tokens = list(map(int, data.split()))
    if not tokens:
        return ""

    t = tokens[0]
    i = 1
    out: List[str] = []

    for _ in range(t):
        # 每組格式：N, P, 接著 P 個 hartal 參數。
        n = tokens[i]
        i += 1
        p = tokens[i]
        i += 1
        hartals = tokens[i:i + p]
        i += p
        out.append(str(count_lost_days(n, hartals)))

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    # 從標準輸入讀完整測資後，一次輸出所有答案。
    print(solve(sys.stdin.read()))
