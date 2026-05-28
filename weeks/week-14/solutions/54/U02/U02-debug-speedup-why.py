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
import math
import timeit
import traceback


# ---------- 14.9 / 14.10 三種拋法的差別 ----------
class AppError(Exception):
    """自訂應用層例外"""
    pass


def low_level():
    """低階函式，拋出基本例外"""
    raise ValueError("低階：值不對")


def variant_a():
    """raise X from e：明確標示「因為 e 所以 X」（推薦用於包裝底層錯誤）"""
    try:
        low_level()
    except ValueError as e:
        # 使用 from 明確指定原始例外，建立例外鏈
        raise AppError("應用層失敗") from e


def variant_b():
    """raise X：context 隱式保留，traceback 會顯示『During handling...』"""
    try:
        low_level()
    except ValueError:
        # 直接拋出新例外，原例外會隱式保留在 __context__
        raise AppError("應用層失敗")


def variant_c_good():
    """bare raise：保留原 traceback；想在中途記 log 又原封不動往上拋時用"""
    try:
        low_level()
    except ValueError:
        print("  [中途記 log]")
        raise  # 重新拋出原例外，保留完整的 traceback


def variant_c_bad():
    """`raise e`：traceback 從這一行重新開始，丟失「真正出事的位置」"""
    try:
        low_level()
    except ValueError as e:
        # 避免這樣做！會丟失原始 traceback
        raise e


def demo_raise_styles():
    """展示三種不同拋法的差異"""
    for name, fn in [("A: raise X from e", variant_a),
                     ("B: raise X (隱式)", variant_b),
                     ("C-good: bare raise", variant_c_good),
                     ("C-bad : raise e", variant_c_bad)]:
        print(f"\n=== {name} ===")
        try:
            fn()
        except Exception:
            # 輸出完整的追蹤訊息
            traceback.print_exc()


# ---------- 14.12 為什麼一定要 print_exc 而不是 print(e) ----------
def demo_print_exc_vs_str():
    """
    print(e) 只給訊息，看不出在哪一行、呼叫鏈是什麼。
    print_exc / format_exc 才有完整 traceback——除錯成本差數十倍。
    """
    def will_crash():
        # 存取不存在的鍵會拋出 KeyError
        data = {"a": 1}
        return data["missing"]

    try:
        will_crash()
    except Exception as e:
        print("【壞示範】print(e)：")
        # 只有訊息，沒有位置資訊
        print(f"  {e}")
        print("【好示範】traceback.print_exc()：")
        # 顯示完整的呼叫堆疊和位置資訊
        traceback.print_exc()


# ---------- 14.14 local 變數為什麼比較快 ----------
def slow_version(items):
    """每# 每次迴圈都要查找全域變數 math 和其屬性 sqrt，較慢
        result.append(math.sqrt(x))
    return result


def fast_version(items):
    """
    sqrt = math.sqrt → LOAD_FAST，比 LOAD_GLOBAL 快
    list comprehension 比 append 少一次 method 查找與呼叫
    """
    sqrt = math.sqrt  # 將方法保存到本地變數
    # 使用本地變數快速存取，且用 list comprehension 更有效率
    return [sqrt(x) for x in items]


def demo_speedup():
    """
    重點：
    1. 先 cProfile 找瓶頸再優化，不要憑感覺。
    2. 微優化（local var、list comp）只在「熱迴圈」有用，
       一般程式可讀性比快幾 ms 重要。
    """
    data = list(range(1, 100_000))  # 準備測試資料
    # 測量慢速版本的執行時間
    t1 = timeit.timeit(lambda: slow_version(data), number=10)
    # 測量快速版本的執行時間
    t2 = timeit.timeit(lambda: fast_version(data), number=10)
    # 展示不同的例外拋法及其追蹤訊息的差異
    print("########## 14.9 / 14.10 三種拋法 ##########")
    demo_raise_styles()

    # 展示正確的例外輸出方式
    print("\n########## 14.12 print_exc vs print(e) ##########")
    demo_print_exc_vs_str()

    # 展示優化技巧的實際效能差異

if __name__ == "__main__":
    print("########## 14.9 / 14.10 三種拋法 ##########")
    demo_raise_styles()

    print("\n########## 14.12 print_exc vs print(e) ##########")
    demo_print_exc_vs_str()

    print("\n########## 14.14 local 變數加速 ##########")
    demo_speedup()
