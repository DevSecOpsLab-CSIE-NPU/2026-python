# 手打程式：手動實現排列生成，並加上繁體中文註解

import sys

# 定義回溯函數來生成排列
def backtrack(current, used, forbidden, N, perms):
    # 如果當前排列長度等於 N，表示找到一個有效排列，加入結果列表
    if len(current) == N:
        perms.append(current[:])
        return
    # 嘗試將每個數字 i 放入當前位置
    for i in range(N):
        # 檢查數字 i 未被使用，且當前位置 (len(current)+1) 不被第 i 個人禁止
        if not used[i] and (len(current) + 1 not in forbidden[i]):
            # 標記數字 i 為已使用
            used[i] = True
            # 將 i 加入當前排列
            current.append(i)
            # 遞歸處理下一個位置
            backtrack(current, used, forbidden, N, perms)
            # 回溯，移除 i
            current.pop()
            # 取消標記
            used[i] = False

def main():
    # 從檔案讀取輸入資料
    with open('test_input_10226.txt', 'r') as f:
        data = f.read().split()
    index = 0
    while index < len(data):
        # 讀取 N
        N = int(data[index])
        index += 1
        # 讀取每個人的禁止位置
        forbidden = []
        for i in range(N):
            f = set()
            while True:
                pos = int(data[index])
                index += 1
                if pos == 0:
                    break
                f.add(pos)
            forbidden.append(f)
        # 生成所有有效排列
        perms = []
        backtrack([], [False] * N, forbidden, N, perms)
        # 輸出到測試記錄檔案
        with open('10226-manual_test.log', 'w') as log:
            prev = None
            for perm in perms:
                # 將排列轉換為字母字串
                s = ''.join(chr(ord('A') + p) for p in perm)
                if prev is None:
                    # 第一個排列，完整輸出
                    log.write(s + '\n')
                    prev = s
                    continue
                # 找到與前一個不同的起始位置
                i = 0
                while i < len(s) and i < len(prev) and s[i] == prev[i]:
                    i += 1
                if i < len(s):
                    # 輸出不同的部分
                    log.write(s[i:] + '\n')
                    prev = s

if __name__ == "__main__":
    main()