#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Big Two 遊戲主程式
"""

import sys
import os

# 添加遊戲目錄到路徑
game_dir = os.path.join(os.path.dirname(__file__), '..', '遊戲')
sys.path.insert(0, game_dir)

def main():
    print("Big Two 遊戲")
    print("這是一個簡單的文字版 Big Two 遊戲實現")
    
    # 這裡可以添加簡單的文字版遊戲邏輯
    # 或者啟動 GUI 版本
    
    print("遊戲模組已載入")
    try:
        from models import Card, Deck, Hand, Player
        from 分類器 import HandClassifier, CardType
        from finder import HandFinder
        from ai import AIStrategy
        from game import BigTwoGame
        
        print("✓ 所有模組載入成功")
        
        # 簡單測試
        deck = Deck()
        print(f"牌組有 {len(deck.cards)} 張牌")
        
        card = Card(14, 3)
        print(f"測試牌: {card}")
        
        hand = Hand([Card(14, 3), Card(13, 2)])
        print(f"手牌: {hand}")
        
        print("基本功能測試通過")
        
    except ImportError as e:
        print(f"✗ 模組載入失敗: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()