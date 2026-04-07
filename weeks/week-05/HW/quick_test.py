#!/usr/bin/env python3
"""簡單測試 HW 項目是否能執行"""

import sys
import os

# 確保在 HW 目錄
hw_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, hw_dir)

print("=" * 60)
print("大貳卡牌遊戲 - 執行測試")
print("=" * 60)
print(f"工作目錄: {hw_dir}")

success_count = 0

# 測試 P1
print("\n[1/6] 測試 P1 - 資料模型...")
try:
    from game.models import Card, Deck, Hand, Player, Suit
    c = Card(5, Suit.SPADES)
    d = Deck()
    h = Hand([c])
    p = Player(0, "Test")
    print("  ✅ P1 可執行")
    success_count += 1
except Exception as e:
    print(f"  ❌ P1 錯誤: {e}")

# 測試 P2
print("[2/6] 測試 P2 - 手牌分類...")
try:
    from game.classifier import CardType, HandClassifier
    clf = HandClassifier()
    result = clf.classify([Card(5, Suit.SPADES)])
    print(f"  ✅ P2 可執行 (分類: {result[0].name})")
    success_count += 1
except Exception as e:
    print(f"  ❌ P2 錯誤: {e}")

# 測試 P3
print("[3/6] 測試 P3 - 手牌搜尋...")
try:
    from game.finder import HandFinder
    finder = HandFinder()
    hand = Hand([Card(3, Suit.SPADES), Card(5, Suit.HEARTS)])
    plays = finder.find_all_plays(hand)
    print(f"  ✅ P3 可執行 (找到 {len(plays)} 個出牌)")
    success_count += 1
except Exception as e:
    print(f"  ❌ P3 錯誤: {e}")

# 測試 P4
print("[4/6] 測試 P4 - AI 策略...")
try:
    from game.ai import AIStrategy
    ai = AIStrategy()
    player = Player(0, "AI")
    player.hand.add_cards([Card(3, Suit.SPADES), Card(5, Suit.HEARTS)])
    play = ai.choose_play(player)
    print(f"  ✅ P4 可執行 (出牌: {len(play) if play else 0} 張)")
    success_count += 1
except Exception as e:
    print(f"  ❌ P4 錯誤: {e}")

# 測試 P5
print("[5/6] 測試 P5 - 遊戲流程...")
try:
    from game.game import BigTwoGame
    game = BigTwoGame(
        player_names=["You", "AI1", "AI2", "AI3"],
        ai_players=[1, 2, 3]
    )
    game.start_game()
    status = game.get_game_status()
    print(f"  ✅ P5 可執行 (玩家: {len(game.players)}, 狀態: {status['state']})")
    success_count += 1
except Exception as e:
    print(f"  ❌ P5 錯誤: {e}")

# 測試 P6
print("[6/6] 測試 P6 - UI 組件...")
try:
    from ui.input import InputHandler
    handler = InputHandler()
    handler.select_card(0)
    print(f"  ✅ P6 可執行 (InputHandler 運作正常)")
    print("  ℹ️  Renderer 需要 pygame + 圖形顯示")
    success_count += 1
except Exception as e:
    print(f"  ❌ P6 錯誤: {e}")

print("\n" + "=" * 60)
print(f"✅ 成功: {success_count}/6 個階段")
print("=" * 60)

if success_count == 6:
    print("\n🎉 所有模塊都可以執行！")
    print("\n要運行完整遊戲 (需要 pygame):")
    print("  pip install pygame")
    print("  python main.py")
    sys.exit(0)
else:
    print(f"\n⚠️  有 {6 - success_count} 個模塊有問題")
    sys.exit(1)
