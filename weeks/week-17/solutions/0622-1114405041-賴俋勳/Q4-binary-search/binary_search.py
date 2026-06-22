"""
題目：二分搜尋功能 - 20分

問題描述：
- 產生序列數據（已排序序列）
- 二分搜尋 vs 線性搜尋的性能比較
- 用 timeit 分別搜尋位置，對比性能
- 產生性能圖並用 README 說明

輸入說明：
- 第一行資料個數 n
- 第二行要搜尋的目標值

輸出說明：
- 搜尋結果位置
- 搜尋耗時

最終需要提交：
- 二分搜尋實作代碼
- 性能對比圖表
- README 說明

學號參數：K = 141（搜尋目標值）
"""

import timeit
import matplotlib.pyplot as plt
import os


def binary_search(arr, target):
    """
    二分搜尋實作
    
    Args:
        arr: 已排序的陣列
        target: 目標值
    
    Returns:
        int: 目標值的索引，未找到返回 -1
    """
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def linear_search(arr, target):
    """
    線性搜尋（用於比較）
    
    Args:
        arr: 陣列
        target: 目標值
    
    Returns:
        int: 目標值的索引，未找到返回 -1
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def compare_search_performance(arr_size=100000, target=None):
    """
    使用 timeit 比較二分搜尋和線性搜尋的性能
    
    Args:
        arr_size: 陣列大小
        target: 搜尋目標值
    
    Returns:
        tuple: (二分搜尋時間, 線性搜尋時間)
    """
    if target is None:
        target = arr_size - 1  # 預設搜尋最後一個元素
    
    arr = list(range(0, arr_size, 2))  # 建立已排序陣列
    
    # 測試二分搜尋
    binary_time = timeit.timeit(
        lambda: binary_search(arr, target),
        number=1000
    )
    
    # 測試線性搜尋
    linear_time = timeit.timeit(
        lambda: linear_search(arr, target),
        number=1000
    )
    
    return binary_time, linear_time


def generate_performance_graph():
    """
    生成性能對比圖表並保存
    
    測試不同陣列大小下的搜尋性能
    """
    print("生成性能圖表中...")
    
    # 測試不同大小的陣列
    sizes = [100, 1000, 10000, 100000, 500000]
    binary_times = []
    linear_times = []
    
    for size in sizes:
        print(f"  測試陣列大小: {size}")
        b_time, l_time = compare_search_performance(size)
        binary_times.append(b_time)
        linear_times.append(l_time)
    
    # 建立圖表
    plt.figure(figsize=(12, 6))
    
    # 子圖1：正常比例
    plt.subplot(1, 2, 1)
    plt.plot(sizes, binary_times, 'o-', label='Binary Search', linewidth=2, markersize=8)
    plt.plot(sizes, linear_times, 's-', label='Linear Search', linewidth=2, markersize=8)
    plt.xlabel('Array Size', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Binary Search vs Linear Search (Normal Scale)', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    # 子圖2：對數比例
    plt.subplot(1, 2, 2)
    plt.loglog(sizes, binary_times, 'o-', label='Binary Search', linewidth=2, markersize=8)
    plt.loglog(sizes, linear_times, 's-', label='Linear Search', linewidth=2, markersize=8)
    plt.xlabel('Array Size (log scale)', fontsize=12)
    plt.ylabel('Time (seconds, log scale)', fontsize=12)
    plt.title('Binary Search vs Linear Search (Log Scale)', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # 建立 assets 資料夾
    os.makedirs('assets', exist_ok=True)
    
    # 保存圖表
    output_path = 'assets/performance_comparison.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"✅ 性能圖表已保存: {output_path}")
    
    # 顯示圖表（可選）
    # plt.show()
    
    plt.close()


def test_k_parameter(k_value=141):
    """
    測試使用學號參數 K=141 進行的搜尋
    
    Args:
        k_value: 搜尋目標值 (預設=141，根據學號1114405041)
    
    Returns:
        dict: 包含搜尋結果和性能數據
    """
    print(f"\n=== K值搜尋測試 (K={k_value}) ===")
    
    # 建立足夠大的陣列來包含 K 值
    arr_size = 500
    arr = list(range(0, arr_size, 2))  # [0, 2, 4, 6, ..., 498]
    
    # 確保 K 值在陣列中
    if k_value not in arr:
        arr.append(k_value)
        arr.sort()
    
    # 執行二分搜尋
    result = binary_search(arr, k_value)
    
    # 性能測試
    b_time, l_time = compare_search_performance(arr_size, k_value)
    
    results = {
        'k_value': k_value,
        'found': result != -1,
        'index': result,
        'binary_time': b_time,
        'linear_time': l_time,
        'speedup': l_time / b_time if b_time > 0 else float('inf')
    }
    
    # 輸出結果
    status = "✅ 找到" if result != -1 else "❌ 未找到"
    print(f"搜尋目標: {k_value} → {status}")
    if result != -1:
        print(f"索引位置: {result}")
    print(f"二分搜尋時間: {b_time:.6f}秒")
    print(f"線性搜尋時間: {l_time:.6f}秒")
    print(f"性能提升: {results['speedup']:.1f}倍")
    
    return results


def main():
    """
    二分搜尋主程式
    
    讀取陣列大小和搜尋目標，執行搜尋
    """
    try:
        # 讀取陣列大小
        n = int(input())
        
        # 生成已排序的陣列 (0 到 n-1)
        arr = list(range(n))
        
        # 讀取要搜尋的目標值
        target = int(input())
        
        # 執行二分搜尋
        result = binary_search(arr, target)
        
        if result != -1:
            print(f"Found at index: {result}")
        else:
            print("Not found")
    
    except EOFError:
        pass


if __name__ == '__main__':
    import sys
    
    # 檢查是否有命令行參數
    if len(sys.argv) > 1:
        if sys.argv[1] == '--performance':
            # 生成性能圖表
            generate_performance_graph()
        elif sys.argv[1] == '--test-k':
            # 測試 K 值搜尋
            k_value = int(sys.argv[2]) if len(sys.argv) > 2 else 141
            test_k_parameter(k_value)
        else:
            print("用法:")
            print("  python binary_search.py              # 標準模式（讀取輸入）")
            print("  python binary_search.py --performance # 生成性能圖表")
            print("  python binary_search.py --test-k [K值] # 測試K值搜尋（預設K=141）")
    else:
        # 標準模式
        main()
