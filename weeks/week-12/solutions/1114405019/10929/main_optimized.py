import sys

# 優化版：直接利用 Python 對大整數的支援與模運算
def solve():
    # 使用 sys.stdin 以迭代方式讀取，對大型輸入更友善
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0":
            break
        if not n_str:
            continue
        
        # Python 本身支援無限位數整數，可以直接轉換並進行模運算
        # 雖然題目建議用位數之和的差判斷，但直接 int(n_str) % 11 在效能上通常更快
        if int(n_str) % 11 == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
