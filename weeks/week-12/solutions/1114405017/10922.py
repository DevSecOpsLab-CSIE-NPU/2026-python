# UVA 10922 — 2 the 9s
# 這個程式判斷輸入的正整數是否為 9 的倍數，並計算其 9 的深度。

def sum_digits(num_str):  # 定義函數計算各位數字總和
    return str(sum(int(d) for d in num_str))  # 將字串轉為數字相加，再轉回字串

def get_degree(num_str):  # 定義函數計算 9 的深度
    degree = 0  # 初始化深度
    original = num_str  # 保存原始輸入
    while len(num_str) > 1:  # 當數字多於一位時
        num_str = sum_digits(num_str)  # 計算各位總和
        degree += 1  # 深度增加
    if num_str == '9':  # 如果最終為 9
        return degree  # 返回深度
    else:  # 否則
        return -1  # 返回 -1 表示不是倍數

# 主程式
import sys  # 匯入 sys 模組
for line in sys.stdin:  # 讀取每一行輸入
    num_str = line.strip()  # 去除空白
    if num_str == '0':  # 如果是 0，結束
        break
    degree = get_degree(num_str)  # 計算深度
    if degree != -1:  # 如果是倍數
        print(f"9-degree of {num_str} is {degree}.")  # 輸出深度
    else:  # 否則
        print(f"{num_str} is not a multiple of 9.")  # 輸出不是倍數