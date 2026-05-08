# 簡單好記憶版本 (Easy version)
import sys

# 計算單一數字的 cycle-length
def get_cycle_length(n):
    # 預設長度為 1，因為至少包含自己
    length = 1
    # 只要還沒跑到 1 就繼續跑
    while n != 1:
        # 如果是奇數，就乘以 3 再加 1
        if n % 2 == 1:
            n = 3 * n + 1
        # 如果是偶數，就除以 2
        else:
            n = n // 2
        # 每做一次動作，長度就加 1
        length += 1
    return length

def main():
    # 讀取標準輸入的每一行 (處理多筆測資)
    for line in sys.stdin:
        # 去除頭尾空白
        line = line.strip()
        # 如果是空行就跳過
        if not line:
            continue
            
        # 拆分兩個數字 i, j
        parts = line.split()
        if len(parts) >= 2:
            i = int(parts[0])
            j = int(parts[1])
            
            # 找出區間的起點與終點 (注意 i 可能大於 j，所以要找 min 和 max)
            start = min(i, j)
            end = max(i, j)
            
            # 用來記錄區間內最大的 cycle length
            max_len = 0
            
            # 遍歷區間內的每個數字
            for num in range(start, end + 1):
                # 取得該數字的 cycle length
                curr_len = get_cycle_length(num)
                # 如果比目前記錄的最大值還大，就更新最大值
                if curr_len > max_len:
                    max_len = curr_len
                    
            # 輸出結果：原來的 i, j 以及區間內最大的 cycle length
            print(f"{i} {j} {max_len}")

if __name__ == "__main__":
    main()
