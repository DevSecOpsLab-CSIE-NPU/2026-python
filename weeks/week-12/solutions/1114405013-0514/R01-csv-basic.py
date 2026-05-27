# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter
#
# CSV（Comma-Separated Values）是最常見的純文字表格格式。
# Python 內建 csv 模組可正確處理逗號、引號、換行等特殊情況，
# 不建議手動用 split(',') 解析，因為欄位內可能包含逗號或引號。

import csv
import io
from typing import TextIO


# ────────────────────────────────────────────────────────────
#  準備範例資料（以字串模擬 CSV 檔案內容）
#  第一列是標頭列，其餘為資料列，逗號分隔。
# ────────────────────────────────────────────────────────────
RAW_CSV: str = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# io.StringIO 把字串包裝成檔案物件，可在記憶體中讀寫，
# 方便教學示範，不必實際建立實體檔案。
# 正式程式碼可用 open('data.csv', 'r') 取代。


# ────────────────────────────────────────────────────────────
#  6.1 csv.reader：逐列讀取，每列回傳 list[str]
#  ─ csv.reader(iterable, delimiter=',', quotechar='"')
#  ─ iterable 可以是檔案、StringIO 或任何可迭代物件
#  ─ 回傳的 reader 本身也是迭代器，可用 next() 或 for 迴圈
# ────────────────────────────────────────────────────────────
def demo_reader(csv_text: str) -> None:
    """
    使用 csv.reader 讀取 CSV：
      - 先用 next() 手動取出第一列作為標頭
      - 再用 for 迴圈迭代其餘資料列
    每列以 list[str] 形式回傳，欄位順序與 CSV 檔案一致。
    """
    print("=== csv.reader ===")
    f: io.StringIO = io.StringIO(csv_text)
    reader = csv.reader(f)          # 建立 reader 物件
    headers: list[str] = next(reader)  # next() 取下一列（第一列 = 標頭）
    print(f"標頭：{headers}")
    for i, row in enumerate(reader, start=1):
        print(f"第 {i} 列：{row}")
    f.close()


# ────────────────────────────────────────────────────────────
#  6.1 csv.DictReader：每列自動對應成 dict
#  ─ 自動將第一列當作鍵（fieldnames），資料列當作值
#  ─ 存取時用 row['欄位名稱']，程式碼更具可讀性
#  ─ 若 CSV 沒有標頭，可傳入 fieldnames 參數手動指定
# ────────────────────────────────────────────────────────────
def demo_dict_reader(csv_text: str) -> None:
    """
    使用 csv.DictReader 讀取 CSV：
      - 自動用第一列建立 fieldnames（欄位名稱）
      - 每列回傳 OrderedDict，可用 row['欄位'] 存取
      - 欄位順序與 CSV 檔案一致
    DictReader 讓程式碼接近資料庫查詢的語意，更易讀。
    """
    print("\n=== csv.DictReader（以 dict 存取）===")
    f: io.StringIO = io.StringIO(csv_text)
    reader = csv.DictReader(f)      # 自動以第一列當 fieldnames
    for i, row in enumerate(reader, start=1):
        # row 是 dict，可用欄位名稱取值，型別為 str
        symbol: str = row['Symbol']
        price: str  = row['Price']
        change: str = row['Change']
        print(f"第 {i} 列：{symbol:5s}  價格={price:>6s}  漲跌={change}")
    f.close()


# ────────────────────────────────────────────────────────────
#  6.1 csv.writer：將資料寫出成 CSV
#  ─ writer.writerow(list)  寫入一列
#  ─ writer.writerows(list_of_list) 一次寫入多列
#  若欄位內含逗號、引號或換行，csv.writer 會自動加上引號跳脫。
# ────────────────────────────────────────────────────────────
def demo_writer() -> None:
    """
    使用 csv.writer 寫出 CSV：
      - 傳入 list，writerow() 依序寫出各欄位
      - 預設以逗號分隔，若有特殊字元自動加引號
      - writerow() 在列尾自動加換行（\\r\\n）
    """
    print("\n=== csv.writer（寫入資料）===")
    output: io.StringIO = io.StringIO()
    writer = csv.writer(output)     # 可傳入檔案物件（如 open('out.csv','w')）

    # writerow() 接受 list，每個元素代表一個欄位
    writer.writerow(['Symbol', 'Price', 'Change'])          # 標頭列
    writer.writerow(['AA', 39.48, -0.18])                   # 資料列 1
    writer.writerow(['AIG', 71.38, -0.15])                  # 資料列 2

    # 含特殊字元的欄位（逗號、引號）會被正確跳脫
    writer.writerow(['BRK.B', 416.50, '+0.02'])             # 含 . 無問題
    writer.writerow(['"特殊"公司', 100.00, '-1.00'])        # 含引號

    print(output.getvalue())  # 輸出寫入結果
    output.close()


# ────────────────────────────────────────────────────────────
#  6.1 csv.DictWriter：以 dict 寫出 CSV
#  ─ 必須指定 fieldnames（欄位順序）
#  ─ writerow(dict) 依照 fieldnames 順序輸出
#  ─ 若 dict 缺少某欄位，該欄位留空；多餘欄位則忽略
# ────────────────────────────────────────────────────────────
def demo_dict_writer() -> None:
    """
    使用 csv.DictWriter 寫出 CSV：
      - 先指明 fieldnames（決定欄位順序）
      - writeheader() 寫出標頭列
      - writerow(dict) 寫出資料列，自動對應欄位名稱
    若資料來源本身就是 dict（如 API 回傳），用 DictWriter 最方便。
    注意：extrasaction='raise' 是預設，遇到未定義欄位會拋錯；
          設為 'ignore' 則靜態忽略多餘欄位。
    """
    print("=== csv.DictWriter（以 dict 寫入）===")
    output: io.StringIO = io.StringIO()
    fieldnames: list[str] = ['Symbol', 'Price', 'Change']

    # DictWriter 需指定 fieldnames，這樣 dict 的鍵才對應到正確的欄位
    # extrasaction='ignore' 讓額外欄位自動被忽略，不拋錯
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()            # 寫出標頭列（依 fieldnames 順序）

    # writerow() 接受 dict，鍵對應欄位名稱
    writer.writerow({'Symbol': 'AA',  'Price': 39.48, 'Change': -0.18})
    writer.writerow({'Symbol': 'AIG', 'Price': 71.38, 'Change': -0.15})

    # 欄位順序與 fieldnames 宣告順序一致，與 dict 傳入順序無關
    # 若 dict 缺少某欄位，該欄位寫入空白
    # 若 dict 含有 fieldnames 之外的鍵，會引發 ValueError
    # （可傳入 extrasaction='ignore' 讓 DictWriter 忽略額外欄位）
    writer.writerow({'Symbol': 'TSLA', 'Price': 245.50})    # 缺少 Change → 空白
    writer.writerow({'Price': 500.00, 'Symbol': 'GOOG',     # 順序不同沒關係
                     'Change': '+2.00'})

    print(output.getvalue())
    output.close()


# ────────────────────────────────────────────────────────────
#  常用參數說明
#  delimiter：分隔字元，預設 ',' → 可用 '\\t' 做 TSV
#  quotechar：引號字元，預設 '"'（跳出含逗號或換行的欄位）
#  quoting：  引號模式
#    csv.QUOTE_ALL       → 每個欄位都加引號
#    csv.QUOTE_MINIMAL   → 僅必要時才加（預設）
#    csv.QUOTE_NONNUMERIC → 非數字欄位加引號
#    csv.QUOTE_NONE      → 不加引號（需自行確保無特殊字元）
# ────────────────────────────────────────────────────────────
def demo_quoting() -> None:
    """
    展示不同的 quoting 模式對輸出結果的影響。
    QUOTE_ALL 常用於需要保留欄位型別的場合（強制所有欄位為字串）。
    """
    print("=== 不同 quoting 模式比較 ===")
    data: list[list[str | float]] = [
        ['Symbol', 'Price', 'Note'],
        ['AA', 39.48, '正常'],
        ['B&B', 50.00, '含&符號'],      # 含 &，但非逗號/引號/換行，可不加引號
        ['C,C', 60.00, '內含,逗號'],     # 含逗號，QUOTE_MINIMAL 會自動加引號
    ]

    for mode, name in [
        (csv.QUOTE_MINIMAL, 'QUOTE_MINIMAL（預設）'),
        (csv.QUOTE_ALL,     'QUOTE_ALL'),
        (csv.QUOTE_NONE,    'QUOTE_NONE（注意：含逗號欄位會拋錯）'),
    ]:
        output: io.StringIO = io.StringIO()
        writer = csv.writer(output, quoting=mode)
        try:
            writer.writerows(data)  # writerows() 一次寫入多列
            print(f"  [{name}]")
            print(f"  {output.getvalue().rstrip()}")
        except csv.Error as e:
            print(f"  [{name}] 錯誤：{e}")
        output.close()


# ────────────────────────────────────────────────────────────
#  示範：含引號與換行的特殊欄位（CSV 跳脫規則）
#  若資料本身含引號，CSV 會用兩個連續引號跳脫（"" → "）
# ────────────────────────────────────────────────────────────
def demo_escape_rules() -> None:
    """
    CSV 跳脫規則展示：
      - 欄位內含逗號 → 整個欄位被引號包住
      - 欄位內含引號 → 用兩個引號跳脫（""）
      - 欄位內含換行 → 整個欄位被引號包住，換行保留
    這些是 csv 模組自動處理的，手動 split(',') 無法正確處理。
    """
    print("\n=== CSV 特殊字元跳脫 ===")
    data: list[list[str]] = [
        ['正常', '欄位', '範例'],
        ['Hello, World', '引號測試"123"', '第三欄'],
        ['多行\n文字', '簡單', '結束'],
    ]

    output: io.StringIO = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)

    # 顯示跳脫後的原貌
    escaped: str = output.getvalue()
    print(f"寫入結果（含跳脫）：\n{escaped}")

    # 重新讀回，驗證跳脫規則正確
    f: io.StringIO = io.StringIO(escaped)
    reader = csv.reader(f)
    print(f"讀回結果：")
    for row in reader:
        print(f"  {row}")
    f.close()
    output.close()


# ────────────────────────────────────────────────────────────
#  主程式：依序執行各示範函式
# ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    demo_reader(RAW_CSV)
    demo_dict_reader(RAW_CSV)
    demo_writer()
    demo_dict_writer()
    demo_quoting()
    demo_escape_rules()
