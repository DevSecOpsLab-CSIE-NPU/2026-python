# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump
#
# JSON（JavaScript Object Notation）是最通用的資料交換格式。
# Python 的 json 模組可無縫轉換 Python 物件 ↔ JSON 字串/檔案。
# 注意：json 模組只支援基本型別（dict/list/str/int/float/bool/None），
# 自訂物件需自行轉換後才能序列化。

import json
from typing import Any, TextIO


# ════════════════════════════════════════════════════════════
#  1. 字串 ↔ Python 物件（核心：json.dumps / json.loads）
# ════════════════════════════════════════════════════════════
# json.dumps(data)    → Python 物件 → JSON 字串（序列化）
# json.loads(s)       → JSON 字串   → Python 物件（反序列化）
# ════════════════════════════════════════════════════════════

def demo_basic_serialization() -> None:
    """
    基本序列化與反序列化（dumps / loads）。

    json.dumps() 支援的 Python 型別：
      dict  → JSON object
      list  → JSON array
      str   → JSON string
      int/float → JSON number
      True/False → JSON true/false
      None  → JSON null
    """
    print("=== 基本序列化（dumps）與反序列化（loads）===")

    # 準備一個 Python dict，包含多種型別
    data: dict[str, Any] = {
        "name": "Alice",
        "age": 30,
        "scores": [95, 87, 92],
        "is_student": False,
        "address": None,
    }

    # 序列化：Python 物件 → JSON 字串
    # 回傳 str，預設無換行、無縮排、ASCII 跳脫
    s: str = json.dumps(data)
    print(f"序列化（dumps）：")
    print(f"  型別：{type(s).__name__}")
    print(f"  內容：{s}")
    print()

    # 反序列化：JSON 字串 → Python 物件
    # 回傳 dict（JSON object → Python dict）
    obj: dict[str, Any] = json.loads(s)
    print(f"反序列化（loads）：")
    print(f"  型別：{type(obj).__name__}")
    print(f"   obj['name']    = {obj['name']}")
    print(f"   obj['scores']  = {obj['scores']}")
    print(f"   obj['address'] = {obj['address']}")


def demo_pretty_print() -> None:
    """
    美化輸出：indent 控制縮排、sort_keys 控制鍵排序。

    參數說明：
      indent      → 縮排空格數（2 或 4 最常見）
      sort_keys   → 按鍵名稱字母排序輸出
      ensure_ascii → 是否跳脫非 ASCII 字元（見下方中文示範）
    """
    print("\n=== 美化輸出（indent / sort_keys）===")
    data: dict[str, Any] = {
        "name": "Bob",
        "age": 25,
        "scores": [88, 76, 95],
        "is_graduate": True,
    }

    # 無美化（一行）
    plain: str = json.dumps(data)
    print(f"無縮排（預設）：\n  {plain}")

    # 有縮排，鍵依字母排序
    pretty: str = json.dumps(data, indent=2, sort_keys=True)
    print(f"美化輸出（indent=2, sort_keys=True）：")
    print(pretty)


def demo_chinese_encoding() -> None:
    """
    中文編碼處理（ensure_ascii 參數）。

    ensure_ascii=True （預設）：
      → 非 ASCII 字元（中文）被跳脫為 \\uXXXX
      → 保證輸出僅含 ASCII，適合老舊系統或純 ASCII 通道

    ensure_ascii=False：
      → 保留原始中文字元
      → 人類可讀，檔案體積較小
    """
    print("\n=== 中文編碼（ensure_ascii）===")
    record: dict[str, Any] = {"城市": "澎湖", "人口": 100000}

    # ensure_ascii=True（預設）：中文被跳脫
    with_ascii: str = json.dumps(record, ensure_ascii=True)
    print(f"ensure_ascii=True  （預設） ：\n  {with_ascii}")

    # ensure_ascii=False：保留原始中文
    without_ascii: str = json.dumps(record, ensure_ascii=False)
    print(f"ensure_ascii=False（可讀） ：\n  {without_ascii}")


# ════════════════════════════════════════════════════════════
#  2. 檔案 I/O（json.dump / json.load）
#  與 dumps/loads 差別在第一個參數是「檔案物件」而非「字串」：
#     json.dump(obj, file)    → 寫入檔案
#     json.load(file)         → 從檔案讀取
#  檔案應以 UTF-8 編碼開啟，以支援多國語言。
# ════════════════════════════════════════════════════════════

def demo_file_io() -> None:
    """
    檔案讀寫（json.dump / json.load）。

    json.dump(obj, file, ...)：
      - 將 Python 物件序列化後直接寫入檔案
      - 接受與 dumps 相同的關鍵字參數（indent, ensure_ascii 等）

    json.load(file)：
      - 從檔案讀取並解析 JSON
      - 回傳 Python 物件（通常是 dict 或 list）

    建議：always 指定 encoding='utf-8'，避免跨平台編碼問題。
    """
    print("\n=== 檔案 I/O（dump / load）===")
    data: dict[str, Any] = {
        "name": "Charlie",
        "age": 28,
        "courses": ["Python", "資料結構", "演算法"],
    }

    # json.dump：寫入檔案（序列化）
    # 使用 /tmp 路徑，無需清理
    filepath: str = "/tmp/demo.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"已寫入檔案：{filepath}")

    # json.load：從檔案讀取（反序列化）
    with open(filepath, "r", encoding="utf-8") as f:
        loaded: dict[str, Any] = json.load(f)

    print(f"從檔案讀入：{loaded}")


# ════════════════════════════════════════════════════════════
#  3. JSON 陣列頂層結構
#  JSON 根層級可以是陣列（list），不限於物件（dict）。
# ════════════════════════════════════════════════════════════

def demo_json_array() -> None:
    """
    JSON 根層級可以是陣列（list），實務上也很常見。
    json 模組可以正確處理 list 頂層。
    """
    print("\n=== JSON 陣列頂層（list 為根）===")
    records: list[dict[str, Any]] = [
        {"name": "Alice", "score": 90},
        {"name": "Bob", "score": 75},
        {"name": "Carol", "score": 88},
    ]

    s: str = json.dumps(records, indent=2, ensure_ascii=False)
    print(f"序列化 list（含 3 筆 dict）：")
    print(s)

    # 反序列化陣列
    loaded: list[dict[str, Any]] = json.loads(s)
    print(f"反序列化回 list，共 {len(loaded)} 筆資料")


# ════════════════════════════════════════════════════════════
#  4. 自訂類別序列化
#  自訂物件無法直接被 json.dumps 序列化，需：
#    方法 A：自訂 __dict__ 或回傳 dict 的方法
#    方法 B：自訂 JSONEncoder
#    方法 C：default 參數 + lambda
# ════════════════════════════════════════════════════════════

class Student:
    """自訂類別，展示如何轉換為 dict 以支援 JSON 序列化。"""

    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def to_dict(self) -> dict[str, Any]:
        """將 Student 實例轉換為 dict，供 json.dumps 使用。"""
        return {"name": self.name, "grade": self.grade}

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, grade={self.grade})"


def demo_custom_serialization() -> None:
    """
    自訂類別的序列化方法：

    方法 1：手動呼叫 obj.to_dict() 再傳給 json.dumps
    方法 2：利用 default 參數提供轉換函式
    方法 3：撰寫自訂 JSONEncoder 子類別（進階）

    json.dumps 遇到無法處理的型別時，會嘗試呼叫 default 參數指定的函式；
    若未提供 default，則拋出 TypeError。
    """
    print("\n=== 自訂類別序列化 ===")

    stu: Student = Student("David", 85)
    print(f"原始物件：{stu}")

    # 方法 1：手動轉換為 dict
    dict_data: dict[str, Any] = stu.to_dict()
    s1: str = json.dumps(dict_data, ensure_ascii=False)
    print(f"方法1（手動 to_dict）：{s1}")

    # 方法 2：利用 default 參數，自動轉換 Student 實例
    s2: str = json.dumps(stu, default=lambda obj: obj.to_dict(),
                         ensure_ascii=False)
    print(f"方法2（default 參數）：{s2}")

    # 若未處理自訂型別，會拋出 TypeError
    try:
        json.dumps(stu)  # Student 不是 json 可序列化的型別
    except TypeError as e:
        print(f"未處理自訂型別時：{e}")


# ════════════════════════════════════════════════════════════
#  5. 錯誤處理
#  不合法 JSON 字串會引發 json.JSONDecodeError
# ════════════════════════════════════════════════════════════

def demo_error_handling() -> None:
    """
    JSONDecodeError 的捕捉與處理。

    json.loads() 遇到格式錯誤的 JSON 時拋出 json.JSONDecodeError，
    它是 ValueError 的子類別，可取得 msg、doc、pos 等除錯資訊。
    """
    print("\n=== JSON 錯誤處理 ===")

    malformed_inputs: list[str] = [
        '{name: "Alice"}',          # 鍵缺少雙引號（不合法的 JSON）
        '{"name": "Alice",}',       # 結尾多餘逗號
        '{"name":}',                # 值缺失
    ]

    for bad_json in malformed_inputs:
        try:
            json.loads(bad_json)
        except json.JSONDecodeError as e:
            print(f"  輸入：{bad_json}")
            print(f"  錯誤：{e}")


# ════════════════════════════════════════════════════════════
#  主程式：依序執行各示範函式
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    demo_basic_serialization()
    demo_pretty_print()
    demo_chinese_encoding()
    demo_file_io()
    demo_json_array()
    demo_custom_serialization()
    demo_error_handling()
