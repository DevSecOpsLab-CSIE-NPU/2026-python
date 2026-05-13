#!/usr/bin/env python3
# 更簡單易記版本（繁體中文註解）
# 思路：若 S < D 或 (S+D) 非偶數 就不可能；否則 高分=(S+D)/2 低分=(S-D)/2
import sys

# 讀取全部輸入並處理
def main():
    parts = sys.stdin.read().strip().split()
    if not parts:
        return
    t = int(parts[0])
    i = 1
    res = []
    for _ in range(t):
        S = int(parts[i]); D = int(parts[i+1]); i += 2
        # 檢查是否有整數解
        if S < D or (S + D) % 2 != 0:
            res.append('impossible')
        else:
            high = (S + D) // 2
            low = (S - D) // 2
            if low < 0:
                res.append('impossible')
            else:
                res.append(f"{high} {low}")
    print('\n'.join(res))

if __name__ == '__main__':
    main()
