"""
U02：例外鏈接、除錯與加速的「為什麼」（理解層）

此檔主要解釋以下幾點：
- 使用 raise ... from ... 與其他拋出例外方式的差別與適用情境
- 為什麼不要用 raise e（會丟失原始 traceback）
- 使用 traceback.print_exc() 能取得完整的呼叫鏈與行號，對除錯非常重要
- 為什麼把全域模組的函式（如 math.sqrt）先綁到 local 變數可以加速

執行：
    python U02-debug-speedup-why.py
"""
import math
import timeit
import traceback


# ---------- 14.9 / 14.10 三種拋法的差別 ----------
class AppError(Exception):
    """應用層自訂例外，示範把底層錯誤包裝後再拋出。"""


def low_level():
    # 模擬底層錯誤
    raise ValueError("低階：值不對")


def variant_a():
    """raise X from e：明確標示「因為 e 所以 X」。

    - 這種方式會在 traceback 中顯示 __cause__，說明兩個例外之間的因果關係，
      對於封裝底層錯誤（例如把 DB/IO 錯誤包成更具意義的應用層錯誤）很有用。
    """
    try:
        low_level()
    except ValueError as e:
        raise AppError("應用層失敗") from e


def variant_b():
    """raise X（不使用 from）：context 隱式保留。

    - traceback 中會包含 'During handling of the above exception, another exception occurred:' 的區塊，
      也能指出原始發生的位置，但語意不如 explicit from 清楚。
    """
    try:
        low_level()
    except ValueError:
        raise AppError("應用層失敗")


def variant_c_good():
    """bare raise：在 except 裡直接使用 raise（不帶任何例外物件），會保留原始 traceback。

    - 適用於你只想在中間記錄或做副作用（例如 logging），但不想改變例外本身與其 traceback。
    """
    try:
        low_level()
    except ValueError:
        print("  [中途記 log]")
        raise


def variant_c_bad():
    """raise e（顯式重拋被捕獲的例外物件）會重設 traceback，導致丟失最原始出錯位置。"""
    try:
        low_level()
    except ValueError as e:
        # 不要這樣做：raise e 會讓 traceback 從這行開始，無法看到 low_level() 的行號
        raise e


def demo_raise_styles():
    """演示各種拋出方式，並列印完整 traceback 以便比較。"""
    for name, fn in [("A: raise X from e", variant_a),
                     ("B: raise X (隱式)", variant_b),
                     ("C-good: bare raise", variant_c_good),
                     ("C-bad : raise e", variant_c_bad)]:
        print(f"\n=== {name} ===")
        try:
            fn()
        except Exception:
            # 使用 traceback.print_exc() 可以得到最完整的 call stack 與行號資訊
            traceback.print_exc()


# ---------- 14.12 為什麼一定要 print_exc 而不是 print(e) ----------
def demo_print_exc_vs_str():
    """示範 print(e) 與 traceback.print_exc() 的差異。

    - print(e) 只顯示例外文字，無法得知發生位置或呼叫鏈。
    - traceback.print_exc() 會輸出完整 traceback，有助於快速定位問題。
    """
    def will_crash():
        data = {"a": 1}
        return data["missing"]

    try:
        will_crash()
    except Exception as e:
        print("【壞示範】print(e)：")
        print(f"  {e}")
        print("【好示範】traceback.print_exc()：")
        traceback.print_exc()


# ---------- 14.14 local 變數為什麼比較快 ----------
def slow_version(items):
    """示範較慢的寫法：每次迴圈都要做全域與屬性查找（LOAD_GLOBAL + LOAD_ATTR）。"""
    result = []
    for x in items:
        result.append(math.sqrt(x))
    return result


def fast_version(items):
    """示範較快的寫法：先把 math.sqrt 綁到 local 變數，並使用 list comprehension。"""
    # 把 math.sqrt 綁到區域變數，LOAD_FAST 比 LOAD_GLOBAL 更快。
    sqrt = math.sqrt
    # list comprehension 通常比顯式 append 更快，因為內部優化與減少方法查找。
    return [sqrt(x) for x in items]


def demo_speedup():
    """以 timeit 比較兩種寫法在大量資料上的耗時，並印出加速比。

    注意：微優化只在熱迴圈中才有明顯效果；在非熱點程式中以可讀性為先。
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
