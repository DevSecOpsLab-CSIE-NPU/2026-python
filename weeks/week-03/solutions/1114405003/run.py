#!/usr/bin/env python
"""
機器人遊戲啟動腳本
簡單執行此檔案即可開始遊戲
"""

from robot_game import RobotGameUI

def main():
    """啟動遊戲"""
    print("="*60)
    print("歡迎使用機器人遊戲 - Scent Navigation")
    print("="*60)
    print()
    print("輸入地圖大小 (預設: 5 5)")
    print("格式: 寬度 高度")
    print("範例: 10 10")
    print()
    
    try:
        size_input = input("輸入地圖大小 (直接按 Enter 使用 5 5): ").strip()
        if size_input:
            parts = size_input.split()
            if len(parts) == 2:
                width, height = int(parts[0]), int(parts[1])
            else:
                print("輸入格式錯誤，使用預設值 5 5")
                width, height = 5, 5
        else:
            width, height = 5, 5
    except (ValueError, IndexError):
        print("輸入錯誤，使用預設值 5 5")
        width, height = 5, 5
    
    print()
    print(f"啟動遊戲... 地圖大小: {width} × {height}")
    print()
    
    # 啟動遊戲
    ui = RobotGameUI(width, height)
    ui.run()


if __name__ == '__main__':
    main()
