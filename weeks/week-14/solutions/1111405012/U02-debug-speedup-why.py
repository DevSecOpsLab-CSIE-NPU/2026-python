"""
U02：例外鏈接、除錯與加速的「為什麼」（理解層）

對應 Cookbook：
- 14.9  捕獲例外後拋出另一個例外（raise ... from ...）
- 14.10 重新拋出被捕獲的例外（bare raise）
- 14.12 除錯基本崩潰錯誤
- 14.14 加速程式運行

核心問題：
- `raise X from e` / `raise X` / bare `raise` 三者差在哪？
- 為什麼 `raise e` 比 bare `raise` 差？
- traceback.print_exc() vs print(e) 為什麼一定要用前者？
- 為什麼把 math.sqrt 提升為 local 變數會比較快？

執行：
    python U02-debug-speedup-why.py
"""
import math  # Python 的數學函式庫
import timeit  # 精確量測程式碼的執行時間
import traceback  # 列印完整的錯誤堆棧追蹤


# ---------- 14.9 / 14.10 三種拋出例外的方式 ----------
# 展示從低層函數一路拋上來的不同方法

class AppError(Exception):
    """自定義的應用層錯誤類別"""
    pass


def low_level():
    """低層函數：演示底層程式碼拋出的錯誤"""
    raise ValueError("低層：值不對")


def variant_a():
    """最推薦方法：使用 `raise X from e` 
    
    明確標記「因為 e 所以 X」，讓上層程式碼清楚知道
    錯誤的因果關係，有助於除錯。
    """
    try:
        low_level()
    except ValueError as e:
        raise AppError("應用層失敗") from e


def variant_b():
    """第二種方法：使用 `raise X`
    
    context 會被隱式保留，但不明確標記因果關係。
    traceback 會顯示「During handling...」提示有連續例外。
    """
    try:
        low_level()
    except ValueError:
        raise AppError("應用層失敗")


def variant_c_good():
    """第三種方法（推薦）：使用 bare raise
    
    完整保留原始 traceback。適合在記錄日誌後
    需要繼續傳遞原始錯誤的場景。
    """
    try:
        low_level()
    except ValueError:
        print("  [中途記 log]")
        raise  # 不修改原始 traceback


def variant_c_bad():
    """第三種方法（不推薦）：使用 `raise e`
    
    traceback 會從這一行重新開始，丟失原始調用堆棧。
    應該改用 bare raise。
    """
    try:
        low_level()
    except ValueError as e:
        raise e  # 不好的做法


def demo_raise_styles():
    """演示三種拋出例外的方法，比較它們的 traceback 輸出"""
    for name, fn in [("A: raise X from e", variant_a),
                     ("B: raise X (隱式)", variant_b),
                     ("C-good: bare raise", variant_c_good),
                     ("C-bad : raise e", variant_c_bad)]:
        print(f"\n=== {name} ===")
        try:
            fn()
        except Exception:
            traceback.print_exc()


# ---------- 14.12 為什麼一定要使用 traceback.print_exc() 而不是 print(e) ----------
def demo_print_exc_vs_str():
    """展示：print(e) 有多大的差異
    
    print(e) 只給你錯誤訊息，沒有行號、沒有呼叫鏈。
    traceback.print_exc() 提供完整的 traceback，有助於快速定位問題。
    除錯成本相差數十倍。
    """
    def will_crash():
        """會崩潰的程式碼：主動調取不存在的 key"""
        data = {"a": 1}  # 字典裡只有 'a' 這一個 key
        return data["missing"]  # 調取不存在的 key → KeyError

    try:
        will_crash()
    except Exception as e:
        print("【壞示範】print(e)：")
        print(f"  {e}")  # 只打印錯誤訊息
        print("【好示範】traceback.print_exc()：")
        traceback.print_exc()  # 列印完整的 traceback


# ---------- 14.14 為什麼把 math.sqrt 提升為 local 變數會比較快 ----------
def slow_version(items):
    """慢速的實現：每次都要接取模組。
    
    每個資料都要執行這些動作：
    1. LOAD_GLOBAL("math") → 從全域符號表恢復變數 math
    2. LOAD_ATTR("sqrt") → 從 math 裡找出 sqrt 函式
    3. 每次都要重複這個過程
    """
    result = []
    for x in items:
        result.append(math.sqrt(x))
    return result


def fast_version(items):
    """快速的實現：優化了多個地方
    
    1. sqrt = math.sqrt → 只做一次 LOAD_ATTR，之後用 LOAD_FAST（更快）
    2. list comprehension 比 append 快，不需要重複做方法查找
    3. 內部變數能直接從 stack 取得，速度更快。
    """
    sqrt = math.sqrt  # 一次性地接取 sqrt 函式
    return [sqrt(x) for x in items]  # 使用 list comprehension


def demo_speedup():
    """實況測量並比較兩種實現的速度差異
    
    重點：
    1. 先用工具找瓶頸再最優化，不要憑感覺。
    2. 微優化（例如 local var、list comp）只在「熱迴圈」有效果。
    3. 不是所有程式都需要微優化：日常程式中，可讀性比快幾毫秒重要。
    """
    data = list(range(1, 100_000))
    t1 = timeit.timeit(lambda: slow_version(data), number=10)
    t2 = timeit.timeit(lambda: fast_version(data), number=10)
    print(f"slow = {t1:.3f}s, fast = {t2:.3f}s, speedup = {t1/t2:.2f}x")


if __name__ == "__main__":
    print("########## 14.9 / 14.10 三種拋法 ##########")
    demo_raise_styles()

    print("\n########## 14.12 print_exc vs print(e) ##########")
    demo_print_exc_vs_str()

    print("\n########## 14.14 local 變數加速 ##########")
    demo_speedup()
