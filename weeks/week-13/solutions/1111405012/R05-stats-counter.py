"""R05. 資料統計與累加（6.13）"""

from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from typing import Iterable, Sequence


WORDS = ["apple", "banana", "apple", "cherry", "banana", "apple"]
RECORDS = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]
SCORES = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
DEPT_SCORE_ROWS = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

Stock = namedtuple("Stock", ["symbol", "price", "change"])


def count_words(words: Iterable[str]) -> Counter[str]:
    """統計每個單字出現次數。"""
    return Counter(words)


def merge_word_counts(counter: Counter[str], extra_words: Iterable[str]) -> Counter[str]:
    """把既有計數結果與額外單字計數合併。"""
    return counter + Counter(extra_words)


def group_members_by_dept(records: Sequence[tuple[str, str]]) -> dict[str, list[str]]:
    """把學生依系所分組。"""
    grouped: defaultdict[str, list[str]] = defaultdict(list)
    for dept, name in records:
        grouped[dept].append(name)
    return dict(grouped)


def sum_scores_by_name(records: Sequence[tuple[str, int]]) -> dict[str, int]:
    """把同一個人的分數累加。"""
    totals: defaultdict[str, int] = defaultdict(int)
    for name, score in records:
        totals[name] += score
    return dict(totals)


def make_stock(symbol: str, price: float, change: float) -> Stock:
    """建立具名股票資料。"""
    return Stock(symbol, price, change)


def calculate_dept_averages(rows: Sequence[dict[str, int | float | str]]) -> dict[str, float]:
    """把每個系所的分數整理後計算平均。"""
    dept_scores: defaultdict[str, list[float]] = defaultdict(list)
    for row in rows:
        dept = str(row["dept"])
        score = float(row["score"])
        dept_scores[dept].append(score)

    averages: dict[str, float] = {}
    for dept, scores in dept_scores.items():
        averages[dept] = sum(scores) / len(scores)
    return averages


def main() -> None:
    """印出課堂上示範的統計結果。"""
    word_counter = count_words(WORDS)
    print("Counter：", word_counter)
    print("最多出現：", word_counter.most_common(2))
    print("合併：", merge_word_counts(word_counter, ["banana", "cherry"]))

    print("\ndefaultdict：")
    for dept, members in group_members_by_dept(RECORDS).items():
        print(f"  {dept}: {members}")

    print("\n各人總分：", sum_scores_by_name(SCORES))

    stock = make_stock("AA", 39.48, -0.18)
    print(f"\n{stock.symbol}: ${stock.price}  漲跌 {stock.change}")

    print("\n各系平均：")
    for dept, average in calculate_dept_averages(DEPT_SCORE_ROWS).items():
        print(f"  {dept}: {average:.1f}")


if __name__ == "__main__":
    main()
