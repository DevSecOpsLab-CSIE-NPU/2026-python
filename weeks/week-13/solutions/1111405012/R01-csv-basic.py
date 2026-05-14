"""R01. CSV 基礎讀寫（6.1）"""

from __future__ import annotations

import csv
import io
from typing import Mapping, Sequence


# 這份字串用來模擬從檔案讀進來的 CSV 內容。
RAW_CSV = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

OUTPUT_FIELDS = ["Symbol", "Price", "Change"]


def read_csv_rows(raw_csv: str) -> tuple[list[str], list[list[str]]]:
    """用 csv.reader 讀取資料，回傳標頭與資料列。"""
    buffer = io.StringIO(raw_csv)
    reader = csv.reader(buffer)
    headers = next(reader, [])
    rows = list(reader)
    return headers, rows


def read_csv_dict_rows(raw_csv: str) -> list[dict[str, str]]:
    """用 csv.DictReader 讀取資料，讓每列直接對應欄位名稱。"""
    buffer = io.StringIO(raw_csv)
    return list(csv.DictReader(buffer))


def write_csv_text(rows: Sequence[Sequence[object]]) -> str:
    """用 csv.writer 產生簡化後的 CSV 文字。"""
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(OUTPUT_FIELDS)
    writer.writerows(rows)
    return output.getvalue()


def write_dict_csv_text(rows: Sequence[Mapping[str, object]]) -> str:
    """用 csv.DictWriter 產生欄位名稱固定的 CSV 文字。"""
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=OUTPUT_FIELDS)
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> None:
    """印出課堂上示範的 CSV 讀寫結果。"""
    headers, rows = read_csv_rows(RAW_CSV)
    print("=== csv.reader ===")
    print("標頭：", headers)
    for row in rows:
        print(row)

    print("\n=== csv.DictReader ===")
    for row in read_csv_dict_rows(RAW_CSV):
        print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

    print("\n=== csv.writer ===")
    print(
        write_csv_text(
            [
                ["AA", 39.48, -0.18],
                ["AIG", 71.38, -0.15],
            ]
        )
    )

    print("=== csv.DictWriter ===")
    print(
        write_dict_csv_text(
            [
                {"Symbol": "AA", "Price": 39.48, "Change": -0.18},
                {"Symbol": "AIG", "Price": 71.38, "Change": -0.15},
            ]
        )
    )

    print("# delimiter='\\t'   → TSV（Tab 分隔）")
    print("# quotechar='\"'    → 引號字元")
    print("# quoting=csv.QUOTE_ALL → 每個欄位都加引號")


if __name__ == "__main__":
    main()
