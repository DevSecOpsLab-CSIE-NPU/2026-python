import sys

# 優化版：使用內建函數與格式化字串簡化流程
def solve():
    # 使用 sys.stdin 以迭代器方式讀取，節省記憶體
    for line in sys.stdin:
        line = line.strip()
        if not line or line == "0":
            break
            
        n = int(line)
        # f"{n:b}" 直接將整數轉為二進位字串，效率優於 bin(n)[2:]
        b_str = f"{n:b}"
        # count("1") 是 C 實作的，速度非常快
        p = b_str.count("1")
        
        print(f"The parity of {b_str} is {p} (mod 2).")

if __name__ == "__main__":
    solve()
