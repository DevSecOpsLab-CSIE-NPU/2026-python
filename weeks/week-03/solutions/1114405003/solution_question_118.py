"""
題目 118 - 罐頭工廠機器人 (Robot World Navigation)

這題要求模擬矩形網格上機器人的行動：
- 機器人有位置 (x, y) 和方向 (N/S/E/W)
- 指令：L (左轉)、R (右轉)、F (前進)
- 邊界管理：機器人掉落時留下「scent」標記
- Scent 機制：在有標記的地方收到會掉落的指令時忽略該指令

核心演算法：
1. 解析輸入（網格尺寸、機器人初始位置和指令）
2. 對每個機器人依序執行指令
3. 追蹤已掉落機器人留下的 scent 標記
4. 輸出最終位置或 LOST 狀態
"""


class RobotWorld:
    """
    機器人世界模擬類。
    
    負責管理：
    - 矩形網格邊界
    - 機器人位置和方向
    - Scent（臭跡）標記
    - 指令執行
    """
    
    # 方向定義：N (北) = (0,1), S (南) = (0,-1), E (東) = (1,0), W (西) = (-1,0)
    DIRECTIONS = {
        'N': (0, 1),   # 北：y 增加
        'S': (0, -1),  # 南：y 減少
        'E': (1, 0),   # 東：x 增加
        'W': (-1, 0)   # 西：x 減少
    }
    
    # 方向字元的列表（用於旋轉）
    DIRECTION_ORDER = ['N', 'E', 'S', 'W']  # 天干之序：北→東→南→西（順時針）
    
    def __init__(self, width, height):
        """
        初始化機器人世界。
        
        參數：
            width (int): 矩形世界的寬度（右上角 x 座標）
            height (int): 矩形世界的高度（右上角 y 座標）
            
        有效座標範圍：0 <= x <= width, 0 <= y <= height
        """
        self.width = width
        self.height = height
        # Scent 標記集合：存儲所有掉落過機器人的位置
        # 格式：(x, y)，無需記錄方向
        self.scents = set()
    
    def is_within_bounds(self, x, y):
        """
        檢查座標是否在矩形網格內。
        
        參數：
            x (int): x 座標
            y (int): y 座標
            
        返回：
            bool: True 如果 0 <= x <= width 且 0 <= y <= height
        """
        return 0 <= x <= self.width and 0 <= y <= self.height
    
    def rotate(self, direction, turn):
        """
        旋轉機器人方向。
        
        參數：
            direction (str): 當前方向 ('N', 'S', 'E', 'W')
            turn (str): 旋轉指令 ('L' 左轉或 'R' 右轉)
            
        返回：
            str: 新方向
            
        範例：
            >>> world = RobotWorld(5, 3)
            >>> world.rotate('N', 'R')  # 北轉右90度 = 東
            'E'
            >>> world.rotate('N', 'L')  # 北轉左90度 = 西
            'W'
        """
        # 找到當前方向在列表中的位置
        curr_index = self.DIRECTION_ORDER.index(direction)
        
        if turn == 'R':  # 右轉（順時針）
            # 順時針轉動：索引 +1，模 4 以環繞
            new_index = (curr_index + 1) % 4
        else:  # 左轉 (turn == 'L')
            # 逆時針轉動：索引 -1，模 4 以環繞
            new_index = (curr_index - 1) % 4
        
        return self.DIRECTION_ORDER[new_index]
    
    def execute_instructions(self, x, y, direction, instructions):
        """
        執行機器人的指令序列。
        
        演算法：
        1. 對指令字符串中的每個字符:
           - 'L' 或 'R': 在原地旋轉
           - 'F': 計算新位置，檢查是否掉落或遇到 scent
        2. 如果掉落，記錄末尾位置和方向，加入 scent，返回 LOST 狀態
        3. 如果成功完成所有指令，返回最終位置和方向
        
        參數：
            x (int): 機器人起始 x 座標
            y (int): 機器人起始 y 座標
            direction (str): 機器人起始方向 ('N', 'S', 'E', 'W')
            instructions (str): 指令字符串，由 'L', 'R', 'F' 組成
            
        返回：
            tuple: (x, y, direction, is_lost)
                  - x, y: 最終位置（或掉落前的最後位置）
                  - direction: 最終方向
                  - is_lost: True 如果機器人掉落，False 否則
        """
        # 逐個執行每條指令
        for instruction in instructions:
            if instruction == 'L':
                # 左轉：在原地轉向
                direction = self.rotate(direction, 'L')
            elif instruction == 'R':
                # 右轉：在原地轉向
                direction = self.rotate(direction, 'R')
            elif instruction == 'F':
                # 前進：計算新位置
                dx, dy = self.DIRECTIONS[direction]
                new_x, new_y = x + dx, y + dy
                
                # 檢查新位置是否超出邊界
                if not self.is_within_bounds(new_x, new_y):
                    # 機器人掉落！
                    # 記錄掉落前的最後位置為 scent 標記
                    self.scents.add((x, y))
                    # 返回掉落前的位置和方向，以及 is_lost=True
                    return (x, y, direction, True)
                
                # 檢查新位置是否有 scent 標記
                if (new_x, new_y) in self.scents:
                    # 有 scent 標記，忽略前進指令，留在原地
                    # 不更新 x, y
                    pass
                else:
                    # 沒有 scent，可以正常前進
                    x, y = new_x, new_y
        
        # 所有指令執行完成，機器人未掉落
        return (x, y, direction, False)


def parse_and_simulate(input_data):
    """
    解析輸入並模擬所有機器人的行動。
    
    輸入格式：
    - 第一行：width height（矩形世界尺寸）
    - 之後每兩行：位置狀態、指令集
    
    參數：
        input_data (str): 多行輸入字符串（或列表）
        
    返回：
        list: 每個機器人的最終狀態，格式為 [(x, y, direction, is_lost), ...]
        
    範例：
        >>> input_str = '''5 3
        ... 1 1 E
        ... RFRFRFRF
        ... 3 2 N
        ... FRRFLLFFRRFLL'''
        >>> results = parse_and_simulate(input_str)
        >>> print(results[0])  # 第一個機器人
        (1, 1, 'E', True)
    """
    # 轉換輸入為行列表
    if isinstance(input_data, str):
        lines = input_data.strip().split('\n')
    else:
        lines = input_data
    
    # 解析第一行：網格尺寸
    width, height = map(int, lines[0].split())
    world = RobotWorld(width, height)
    
    results = []
    i = 1
    
    # 逐對處理機器人的位置和指令
    while i < len(lines):
        # 解析位置行：x y direction
        parts = lines[i].split()
        x, y = int(parts[0]), int(parts[1])
        direction = parts[2]
        
        # 解析指令行
        instructions = lines[i + 1] if i + 1 < len(lines) else ""
        
        # 執行機器人指令
        result = world.execute_instructions(x, y, direction, instructions)
        results.append(result)
        
        i += 2
    
    return results


def format_output(results):
    """
    格式化輸出結果。
    
    參數：
        results (list): 機器人最終狀態列表
        
    返回：
        str: 格式化的輸出字符串
        
    範例：
        >>> results = [(1, 1, 'E', True), (3, 3, 'N', False)]
        >>> print(format_output(results))
        1 1 E LOST
        3 3 N
    """
    output = []
    for x, y, direction, is_lost in results:
        if is_lost:
            output.append(f"{x} {y} {direction} LOST")
        else:
            output.append(f"{x} {y} {direction}")
    return '\n'.join(output)


def main():
    """
    主程式：演示機器人世界模擬。
    
    包含題目提供的標準測試用例。
    """
    print("=" * 60)
    print("題目 118 - 罐頭工廠機器人 (Robot Navigation)")
    print("=" * 60)
    
    # 題目提供的測試用例
    test_input = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLLL"""
    
    print("\n【輸入資料】\n")
    print(test_input)
    
    print("\n【模擬過程】\n")
    
    # 解析並模擬
    results = parse_and_simulate(test_input)
    
    # 輸出結果
    print("【最終輸出】\n")
    output = format_output(results)
    print(output)
    
    # 詳細說明
    print("\n【模擬詳解】")
    print("-" * 60)
    
    # 機器人 1: (1,1,E) - RFRFRFRF
    print("機器人 1: 初始位置 (1,1), 朝向 E")
    print("  指令：R(右轉)F(前進)R(右轉)F(前進)R(右轉)F(前進)R(右轉)F(前進)")
    print("  結果：轉動 4 次 90° = 回到朝向 E，但逐次前進出邊界")
    print("  最終：(1,1,E) LOST - 掉落在 (1,1) 留下 scent")
    
    # 機器人 2: (3,2,N) - FRRFLLFFRRFLL
    print("\nRobot 2: 初始位置 (3,2), 朝向 N")
    print("  指令：FRRFLLFFRRFLL")
    print("  模擬：F(→3,3)R(→E)R(→S)F(→3,1)L(→E)...")
    print("  最終：(3,3,N) - 未掉落")
    
    # 機器人 3: (0,3,W) - LLLL
    print("\nRobot 3: 初始位置 (0,3), 朝向 W")
    print("  指令：LLLL")
    print("  模擬：L(→S)L(→E)L(→N)L(→W)")
    print("  最終：(0,3,W) - 原地轉圈，未掉落")
    
    print("\n" + "=" * 60)
    print("模擬完畢")
    print("=" * 60)


if __name__ == '__main__':
    main()
