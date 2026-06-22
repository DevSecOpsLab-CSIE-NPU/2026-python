import timeit
import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# 1. 產生升冪排序的整數陣列
N = 100000
# 為了確保能找到, 讓數值範圍涵蓋 153 並且有足夠的大小差距
# 我們建立一個包含 0 到 200000 之間的奇數或特定間隔, 
# 這裡簡單用範圍整數確保 153 必定在其中
arr = list(range(0, N * 2, 2)) # 產生偶數陣列
# 強制把 153 放進去，或者我們直接用連續整數確保存在與位置隨機
arr = list(range(1, N + 1)) 

target = 153 # K = 100 + 53

# 2. 實作二分搜尋（計算比較次數）
def binary_search(array, k):
    low = 0
    high = len(array) - 1
    cmp_count = 0
    
    while low <= high:
        cmp_count += 1
        mid = (low + high) // 2
        if array[mid] == k:
            return mid, cmp_count
        elif array[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1, cmp_count

# 為了比對，也寫一個簡單的線性搜尋計算比較次數
def linear_search_cmp(array, k):
    cmp_count = 0
    for i in range(len(array)):
        cmp_count += 1
        if array[i] == k:
            return i, cmp_count
    return -1, cmp_count

# 執行搜尋並輸出結果
idx, cmp_bin = binary_search(arr, target)
if idx != -1:
    print(f"FOUND {idx} cmp={cmp_bin}")
else:
    print(f"NOT FOUND cmp={cmp_bin}")

# 3. 用 timeit 量測效能
# 為了避免線性搜尋在前面太快找到，我們用完整跑完或多次量測的平均
# linear_search 的原生實作供 timeit 使用
def run_linear():
    for x in arr:
        if x == target:
            break

def run_binary():
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

# 由於二分搜尋極快，我們讓它執行較多次數以利量測
t_linear = timeit.timeit(run_linear, number=100)
t_binary = timeit.timeit(run_binary, number=100)

print(f"linear: {t_linear:.6f} s")
print(f"binary: {t_binary:.6f} s")

if t_binary < t_linear:
    print("binary faster")
else:
    print("linear faster")