"""R01 CSV 基礎讀寫詳細註解版。"""

import csv
import io


RAW_CSV = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""


def main():
    # StringIO 可以把字串當成檔案來讀，
    # 這樣就能直接交給 csv.DictReader 使用。
    buffer = io.StringIO(RAW_CSV)

    # DictReader 會把每一列資料轉成字典，
    # key 就是第一列標頭，例如 Symbol、Price、Change。
    rows = list(csv.DictReader(buffer))

    print("=== 讀取 ===")
    for row in rows:
        # 取值時直接用欄位名稱，比記索引位置容易。
        print(row["Symbol"], row["Price"], row["Change"])

    # 如果要再輸出成新的 CSV，也先準備一個記憶體中的檔案。
    output = io.StringIO(newline="")

    # DictWriter 需要先告訴它欄位順序。
    writer = csv.DictWriter(output, fieldnames=["Symbol", "Price", "Change"])
    writer.writeheader()

    # 這裡只示範把前兩筆資料重新寫出去。
    for row in rows[:2]:
        writer.writerow(
            {
                "Symbol": row["Symbol"],
                "Price": row["Price"],
                "Change": row["Change"],
            }
        )

    print("\n=== 寫出 ===")
    print(output.getvalue())


if __name__ == "__main__":
    main()
