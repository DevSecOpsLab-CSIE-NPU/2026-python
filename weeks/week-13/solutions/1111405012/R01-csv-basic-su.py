"""R01 CSV 基礎讀寫簡化版。"""

import csv
import io


RAW_CSV = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""


def main():
    # 讀取：直接把每列轉成 dict，比較好記。
    rows = list(csv.DictReader(io.StringIO(RAW_CSV)))
    print("=== 讀取 ===")
    for row in rows:
        print(row["Symbol"], row["Price"], row["Change"])

    # 寫出：只保留三個欄位。
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=["Symbol", "Price", "Change"])
    writer.writeheader()
    for row in rows[:2]:
        writer.writerow(
            {"Symbol": row["Symbol"], "Price": row["Price"], "Change": row["Change"]}
        )
    print("\n=== 寫出 ===")
    print(output.getvalue())


if __name__ == "__main__":
    main()
