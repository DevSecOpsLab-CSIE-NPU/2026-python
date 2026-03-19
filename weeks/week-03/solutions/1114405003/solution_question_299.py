"""
題目 299 - 火車車廂置換 (Train Swapping)

這題要求計算將火車車廂按照編號 1 到 L 的順序排好所需的最小交換次數。
使用相鄰車廂交換（冒泡排序），計算所有需要的交換次數。

核心算法：
1. 讀取測資數量 N
2. 對每組測資：
   - 讀取火車長度 L
   - 讀取車廂的當前順序（L 個整數）
   - 使用冒泡排序計算交換次數
   - 輸出結果：\"Optimal train swapping takes S swaps.\"

應用場景：計算排序數組所需的最小交換操作數
"""


class TrainSwapper:
    """
    火車車廂置換計算類。
    
    特點：
    - 計算將亂序車廂排序所需的交換次數
    - 使用冒泡排序算法
    - 只統計交換次數，不實際修改數組
    """
    
    def __init__(self):
        """初始化 TrainSwapper 實例。"""
        pass
    
    def count_swaps(self, cars):
        """
        計算排序一組車廂所需的交換次數。
        
        參數：
            cars (list): 車廂編號列表，表示當前順序
                        應包含 1 到 len(cars) 的所有整數
        
        返回：
            int: 將車廂按 1 到 L 順序排好所需的交換次數
        
        演算法：
        使用冒泡排序，統計交換操作的次數。
        對於每一趟，比較相鄰元素，如果需要交換則計數。
        
        時間複雜度：O(n^2)，其中 n 是車廂數量
        空間複雜度：O(1)（不計輸入）
        """
        cars_copy = cars.copy()
        swap_count = 0
        n = len(cars_copy)
        
        # 冒泡排序
        for i in range(n):
            for j in range(n - 1 - i):
                if cars_copy[j] > cars_copy[j + 1]:
                    # 交換並計數
                    cars_copy[j], cars_copy[j + 1] = cars_copy[j + 1], cars_copy[j]
                    swap_count += 1
        
        return swap_count
    
    def process_input(self, lines):
        """
        處理輸入行並計算每組測資的結果。
        
        參數：
            lines (list): 輸入行的列表
        
        返回：
            list: 每組測資的結果字符串
        """
        results = []
        num_cases = int(lines[0].strip())
        
        line_idx = 1
        for _ in range(num_cases):
            length = int(lines[line_idx].strip())
            line_idx += 1
            
            if length == 0:
                results.append("Optimal train swapping takes 0 swaps.")
            else:
                cars = list(map(int, lines[line_idx].strip().split()))
                line_idx += 1
                
                swaps = self.count_swaps(cars)
                results.append(f"Optimal train swapping takes {swaps} swaps.")
        
        return results


def solve_train_swapping(input_text):
    """
    求解火車車廂置換問題的主函式。
    
    參數：
        input_text (str): 完整的輸入文本
    
    返回：
        str: 所有測資的結果，每個結果占一行
    """
    swapper = TrainSwapper()
    lines = input_text.strip().split('\n')
    results = swapper.process_input(lines)
    return '\n'.join(results)


if __name__ == "__main__":
    # 測試範例
    test_input = """1
3
2 3 1"""
    
    output = solve_train_swapping(test_input)
    print(output)
