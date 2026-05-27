# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用

from collections import Counter, defaultdict, namedtuple
from typing import List, Tuple, Dict, Any

# ------------------------------------------------------------
# Counter：計數器，用於計算元素出現次數
# ------------------------------------------------------------
def demo_counter(words: List[str]) -> Counter:
    """示範 Counter 的基本功能：建立計數、取得最常出現項目、合併 Counter。"""
    cnt = Counter(words)
    print("Counter：", cnt)
    print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

    # Counter 也可以直接相加，表示合併計數結果
    extra = Counter(["banana", "cherry"])
    print("合併：", cnt + extra)
    return cnt


def group_by_department(records: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    """將記錄依照系所分組。"""
    by_dept: Dict[str, List[str]] = defaultdict(list)
    for dept, name in records:
        by_dept[dept].append(name)
    return by_dept


def accumulate_scores(scores: List[Tuple[str, int]]) -> Dict[str, int]:
    """用 defaultdict(int) 將各人成績進行累加。"""
    score_sum: Dict[str, int] = defaultdict(int)
    for name, score in scores:
        score_sum[name] += score
    return score_sum


# ------------------------------------------------------------
# namedtuple：具名元組，可讀性更佳
# ------------------------------------------------------------
Stock = namedtuple("Stock", ["symbol", "price", "change"])


def print_stock_example() -> None:
    """示範 namedtuple 的使用方式。"""
    s = Stock("AA", 39.48, -0.18)
    print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")


# ------------------------------------------------------------
# 綜合應用：從 list of dict 做統計，計算各系平均分數
# ------------------------------------------------------------
def calculate_dept_averages(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """計算每個系的平均分數。"""
    dept_scores: Dict[str, List[int]] = defaultdict(list)
    for row in data:
        dept_scores[row["dept"]].append(row["score"])

    dept_avg: Dict[str, float] = {}
    for dept, scores in dept_scores.items():
        dept_avg[dept] = sum(scores) / len(scores)
    return dept_avg


def main() -> None:
    # Counter 範例
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    demo_counter(words)

    # defaultdict(list)：按系所分組
    records = [
        ("系資", "Alice"),
        ("電子", "Bob"),
        ("系資", "Carol"),
        ("電子", "David"),
        ("系資", "Eve"),
    ]
    by_dept = group_by_department(records)
    print("\ndefaultdict：")
    for dept, members in by_dept.items():
        print(f"  {dept}: {members}")

    # defaultdict(int)：成績累加
    scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
    score_sum = accumulate_scores(scores)
    print("\n各人總分：", dict(score_sum))

    # namedtuple 範例
    print_stock_example()

    # list of dict 統計
    data = [
        {"dept": "系資", "score": 85},
        {"dept": "電子", "score": 78},
        {"dept": "系資", "score": 92},
        {"dept": "電子", "score": 88},
    ]
    averages = calculate_dept_averages(data)
    print("\n各系平均：")
    for dept, avg in averages.items():
        print(f"  {dept}: {avg:.1f}")


if __name__ == "__main__":
    main()
