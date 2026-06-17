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
    pass


def low_level():
    raise ValueError("低階：值不對")


def variant_a():
    """raise X from e：明確標示「因為 e 所以 X」（推薦用於包裝底層錯誤）"""
    try:
        low_level()
    except ValueError as e:
        raise AppError("應用層失敗") from e


def variant_b():
    """raise X：context 隱式保留，traceback 會顯示『During handling...』"""
    try:
        low_level()
    except ValueError:
        raise AppError("應用層失敗")


def variant_c_good():
    """bare raise：保留原 traceback；想在中途記 log 又原封不動往上拋時用"""
    try:
        low_level()
    except ValueError:
        print("  [中途記 log]")
        raise


def variant_c_bad():
    """`raise e`：traceback 從這一行重新開始，丟失「真正出事的位置」"""
    try:
        low_level()
    except ValueError as e:
        raise e


def demo_raise_styles():
    for name, fn in [("A: raise X from e", variant_a),
                     ("B: raise X (隱式)", variant_b),
                     ("C-good: bare raise", variant_c_good),
                     ("C-bad : raise e", variant_c_bad)]:
        print(f"\n=== {name} ===")
        try:
            fn()
        except Exception:
            traceback.print_exc()


# ---------- 14.12 為什麼一定要 print_exc 而不是 print(e) ----------
def demo_print_exc_vs_str():
    """
    print(e) 只給訊息，看不出在哪一行、呼叫鏈是什麼。
    print_exc / format_exc 才有完整 traceback——除錯成本差數十倍。
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
    """每次都要做 LOAD_GLOBAL（math）+ LOAD_ATTR（sqrt）"""
    result = []
    for x in items:
        result.append(math.sqrt(x))
    return result


def fast_version(items):
    """
    sqrt = math.sqrt → LOAD_FAST，比 LOAD_GLOBAL 快
    list comprehension 比 append 少一次 method 查找與呼叫
    """
    sqrt = math.sqrt
    return [sqrt(x) for x in items]


def demo_speedup():
    """
    重點：
    1. 先 cProfile 找瓶頸再優化，不要憑感覺。
    2. 微優化（local var、list comp）只在「熱迴圈」有用，
       一般程式可讀性比快幾 ms 重要。
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
