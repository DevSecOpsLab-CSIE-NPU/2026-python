# UVA 10931 — Parity
# 這個程式計算輸入整數的二進位表示中 1 的個數（parity），並輸出指定格式。

import sys  # 匯入 sys 模組，用於讀取標準輸入

for line in sys.stdin:  # 讀取每一行輸入
    I = int(line.strip())  # 轉換為整數
    if I == 0:  # 如果是 0，結束
        break
    B = bin(I)[2:]  # 轉換為二進位字串，移除 '0b' 前綴
    P = B.count('1')  # 計算 1 的個數
    print(f"The parity of {B} is {P} (mod 2).")  # 輸出結果