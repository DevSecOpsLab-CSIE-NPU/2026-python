"""
更簡潔易記版本的 Beat the Spread! 實作

此檔提供 `compute_scores(S, D)`，以最直觀的條件檢查與運算實作。
註解精簡，方便在考場或練習時快速記憶。
"""

def compute_scores(S: int, D: int):
    """簡潔版：直接檢查必要條件並回傳整數解或丟出 ValueError。"""
    # 必要條件：S >= D、S+D 為偶數
    if S < D or (S + D) & 1:
        raise ValueError("impossible")
    hi = (S + D) // 2
    lo = S - hi
    if lo < 0:
        raise ValueError("impossible")
    return hi, lo


if __name__ == "__main__":
    # 簡單 CLI：從 stdin 讀取同題目格式的多組輸入並輸出結果
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        S = int(next(it)); D = int(next(it))
        try:
            h, l = compute_scores(S, D)
            out.append(f"{h} {l}")
        except ValueError:
            out.append("impossible")
    print("\n".join(out))
