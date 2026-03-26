"""
Phase 5: 遊戲流程 - 單元測試

測試 BigTwoGame 類的初始化、出牌流程、回合判定和獲勝條件
實現完整的大老二遊戲邏輯
"""

import unittest
from enum import Enum
from typing import List, Optional, Tuple
from collections import deque


# ==================== 枚舉定義 ====================

class Suit(Enum):
    """花色列舉"""
    CLUB = 0      # ♣ 梅花
    DIAMOND = 1   # ♦ 方塊
    HEART = 2     # ♥ 紅心
    SPADE = 3     # ♠ 黑桃


class CardType(Enum):
    """牌型列舉"""
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9


# ==================== 基礎類別 ====================

class Card:
    """撲克牌"""
    
    def __init__(self, rank: int, suit: int):
        """初始化撲克牌
        
        Args:
            rank: 牌點數 (3-14，其中 14=A, 2=最大)
            suit: 花色 (0=♣, 1=♦, 2=♥, 3=♠)
        """
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        """檢查兩張牌是否相等"""
        return self.rank == other.rank and self.suit == other.suit
    
    def __repr__(self):
        """牌的字符串表示"""
        rank_str = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 2: '2'}.get(self.rank, str(self.rank))
        suit_str = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}.get(self.suit, '?')
        return f"{suit_str}{rank_str}"
    
    def __hash__(self):
        """使卡牌可被雜湊"""
        return hash((self.rank, self.suit))
    
    def __lt__(self, other):
        """用於排序的比較運算符"""
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit


class Hand:
    """牌手"""
    
    def __init__(self, cards: List[Card]):
        """初始化牌手
        
        Args:
            cards: 牌的列表
        """
        self.cards = list(cards)
    
    def remove_cards(self, cards_to_remove: List[Card]) -> 'Hand':
        """從手牌中移除指定的牌
        
        Args:
            cards_to_remove: 要移除的牌列表
            
        Returns:
            新的 Hand 物件（去除指定的牌）
        """
        remaining = self.cards.copy()
        for card in cards_to_remove:
            remaining.remove(card)
        return Hand(remaining)
    
    def __repr__(self):
        """手牌的字符串表示"""
        return f"Hand({self.cards})"


class Deck:
    """牌堆"""
    
    def __init__(self):
        """初始化牌堆（52張牌）"""
        self.cards = []
        self._initialize_deck()
    
    def _initialize_deck(self):
        """初始化標準52張牌堆"""
        for suit in range(4):
            # 加入 3-14 的牌
            for rank in range(3, 15):  # 3-14 (3, 4, 5, 6, 7, 8, 9, 10, J=11, Q=12, K=13, A=14)
                self.cards.append(Card(rank, suit))
            # 加入 rank=2 的牌（最大的牌）
            self.cards.append(Card(2, suit))
    
    def shuffle(self):
        """洗牌"""
        import random
        random.shuffle(self.cards)
    
    def deal(self, num_cards: int) -> List[Card]:
        """從牌堆抽取指定數量的牌
        
        Args:
            num_cards: 要抽取的牌數
            
        Returns:
            抽取的牌列表
        """
        cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return cards


class Player:
    """遊戲玩家"""
    
    def __init__(self, name: str, is_human: bool = False):
        """初始化玩家
        
        Args:
            name: 玩家名稱
            is_human: 是否為人類玩家
        """
        self.name = name
        self.is_human = is_human
        self.hand = Hand([])
    
    def receive_cards(self, cards: List[Card]):
        """接收牌
        
        Args:
            cards: 牌的列表
        """
        self.hand.cards.extend(cards)
        self.hand.cards.sort()
    
    def play_cards(self, cards: List[Card]):
        """出牌（移除手牌中的牌）
        
        Args:
            cards: 要出的牌列表
        """
        for card in cards:
            self.hand.cards.remove(card)
    
    def __repr__(self):
        """玩家的字符串表示"""
        return f"Player({self.name}, {len(self.hand.cards)} cards)"


# ==================== 遊戲類別 ====================

class BigTwoGame:
    """大老二遊戲主類別
    
    負責：
    1. 遊戲初始化（玩家、牌堆、分發牌）
    2. 出牌流程控制
    3. 回合輪轉管理
    4. 獲勝條件檢查
    5. 遊戲狀態管理
    """
    
    # 每人收到的牌數
    CARDS_PER_PLAYER = 13
    
    # 玩家數量
    NUM_PLAYERS = 4
    
    # 首先出牌的玩家必須有梅花3
    FIRST_CARD = Card(3, Suit.CLUB.value)  # ♣3
    
    def __init__(self, human_player_name: str = "玩家"):
        """初始化遊戲
        
        Args:
            human_player_name: 人類玩家的名稱
        """
        self.players: List[Player] = []
        self.current_player_idx = 0
        self.last_play: Optional[List[Card]] = None
        self.last_play_classification: Optional[Tuple] = None
        self.pass_count = 0
        self.is_game_over = False
        self.winner: Optional[Player] = None
        self.human_player_name = human_player_name
        
        # 初始化遊戲
        self._setup_players()
        self._setup_game()
    
    def _setup_players(self):
        """設置玩家（1人類 + 3 AI）"""
        # 【準備】1個人類玩家 + 3個 AI
        self.players = [
            Player(self.human_player_name, is_human=True),
            Player("CPU-1", is_human=False),
            Player("CPU-2", is_human=False),
            Player("CPU-3", is_human=False)
        ]
    
    def _setup_game(self):
        """初始化遊戲（洗牌、分牌、設定首位玩家）"""
        # 【準備】洗牌和分發
        deck = Deck()
        deck.shuffle()
        
        # 分發牌給每位玩家
        for i, player in enumerate(self.players):
            cards = deck.deal(self.CARDS_PER_PLAYER)
            player.receive_cards(cards)
        
        # 【設定】首位玩家為有 ♣3 的玩家
        for idx, player in enumerate(self.players):
            if self.FIRST_CARD in player.hand.cards:
                self.current_player_idx = idx
                break
    
    def get_current_player(self) -> Player:
        """取得當前玩家
        
        Returns:
            當前玩家
        """
        return self.players[self.current_player_idx]
    
    def play(self, cards: List[Card]) -> bool:
        """當前玩家出牌
        
        Args:
            cards: 要出的牌列表
            
        Returns:
            出牌是否成功
        """
        if self.is_game_over:
            return False
        
        current_player = self.get_current_player()
        
        # 檢查牌是否在玩家手中
        for card in cards:
            if card not in current_player.hand.cards:
                return False
        
        # 【執行】出牌
        current_player.play_cards(cards)
        self.last_play = cards
        self.pass_count = 0  # 重置過牌計數
        
        # 檢查遊戲是否結束
        self._check_winner()
        
        # 輪到下家
        self.next_turn()
        return True
    
    def pass_turn(self) -> bool:
        """當前玩家過牌
        
        Returns:
            過牌是否成功
        """
        if self.is_game_over:
            return False
        
        self.pass_count += 1
        
        # 3人過牌時，重置出牌規則
        if self.pass_count >= 3:
            self.last_play = None
            self.last_play_classification = None
            self.pass_count = 0
        
        # 輪到下家
        self.next_turn()
        return True
    
    def next_turn(self):
        """進行下一回合（輪轉到下家）"""
        self.current_player_idx = (self.current_player_idx + 1) % self.NUM_PLAYERS
    
    def _check_winner(self):
        """檢查是否有獲勝者"""
        for player in self.players:
            if len(player.hand.cards) == 0:
                self.is_game_over = True
                self.winner = player
                return
    
    def get_winner(self) -> Optional[Player]:
        """取得獲勝者
        
        Returns:
            獲勝的玩家，若遊戲未結束回傳 None
        """
        return self.winner if self.is_game_over else None
    
    def get_game_status(self) -> dict:
        """取得遊戲狀態
        
        Returns:
            包含遊戲狀態的字典
        """
        return {
            'is_game_over': self.is_game_over,
            'current_player': self.get_current_player().name,
            'winner': self.winner.name if self.winner else None,
            'players_cards': {p.name: len(p.hand.cards) for p in self.players},
            'last_play': self.last_play,
            'pass_count': self.pass_count
        }


# ==================== 單元測試 ====================

class TestGameInitialization(unittest.TestCase):
    """測試遊戲初始化 (BigTwoGame.__init__ 和 _setup_game)
    
    驗證：
    1. 玩家數量
    2. 每人牌數
    3. 總牌數
    4. 首位玩家
    5. 玩家組成
    """
    
    def test_game_has_4_players(self):
        """【測試1】遊戲初始化後有4位玩家
        
        給定：新遊戲
        預期：有4位玩家（1人類+3AI）
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【驗證】
        self.assertEqual(len(game.players), 4, "遊戲應有4位玩家")
    
    def test_each_player_13_cards(self):
        """【測試2】每位玩家有13張牌
        
        給定：遊戲設置後
        預期：4位玩家各有13張牌
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【驗證】
        for player in game.players:
            self.assertEqual(len(player.hand.cards), 13, 
                           f"{player.name} 應有13張牌")
    
    def test_total_cards_distributed(self):
        """【測試3】分發了52張牌
        
        給定：遊戲設置後
        預期：總共分發52張牌 (4 × 13)
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【執行】計算總牌數
        total_cards = sum(len(p.hand.cards) for p in game.players)
        
        # 【驗證】
        self.assertEqual(total_cards, 52, "應分發52張牌")
    
    def test_first_player_has_3_clubs(self):
        """【測試4】首位玩家有梅花3
        
        給定：遊戲設置後
        預期：當前玩家手牌中有 ♣3
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【執行】取得首位玩家
        first_player = game.get_current_player()
        has_club_3 = Card(3, Suit.CLUB.value) in first_player.hand.cards
        
        # 【驗證】
        self.assertTrue(has_club_3, "首位玩家應有 ♣3")
    
    def test_one_human_three_ai(self):
        """【測試5】1位人類玩家 + 3位 AI
        
        給定：遊戲初始化
        預期：1人類玩家，3位 AI 玩家
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【執行】計算人類和 AI 玩家數
        human_count = sum(1 for p in game.players if p.is_human)
        ai_count = sum(1 for p in game.players if not p.is_human)
        
        # 【驗證】
        self.assertEqual(human_count, 1, "應有1位人類玩家")
        self.assertEqual(ai_count, 3, "應有3位 AI 玩家")


class TestPlayRound(unittest.TestCase):
    """測試出牌流程 (BigTwoGame.play 和 pass_turn)
    
    驗證：
    1. 出牌移除手牌
    2. 設定 last_play
    3. 非法出牌被拒絕
    4. 過牌計數
    """
    
    def test_play_removes_cards(self):
        """【測試6】出牌移除手牌中的牌
        
        給定：玩家有牌，執行出牌
        預期：手牌減少
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        player = game.get_current_player()
        initial_count = len(player.hand.cards)
        
        # 出梅花3（首位玩家必有）
        card_to_play = Card(3, Suit.CLUB.value)
        
        # 【執行】
        game.play([card_to_play])
        
        # 【驗證】
        self.assertEqual(len(player.hand.cards), initial_count - 1,
                        "出牌後手牌應減少1張")
    
    def test_play_sets_last_play(self):
        """【測試7】出牌設定 last_play
        
        給定：玩家出牌
        預期：game.last_play 被設定
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        player = game.get_current_player()
        card_to_play = Card(3, Suit.CLUB.value)
        
        # 【執行】
        game.play([card_to_play])
        
        # 【驗證】
        self.assertIsNotNone(game.last_play, "last_play 應被設定")
        self.assertEqual(game.last_play, [card_to_play],
                        "last_play 應為出牌")
    
    def test_invalid_play_returns_false(self):
        """【測試8】非法出牌被拒絕
        
        給定：玩家出不在手牌中的牌
        預期：回傳 False，手牌不變
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        player = game.get_current_player()
        initial_count = len(player.hand.cards)
        
        # 尋找一張不在玩家手牌中的牌
        fake_card = Card(15, 0)  # 不存在的牌
        
        # 【執行】
        result = game.play([fake_card])
        
        # 【驗證】
        self.assertFalse(result, "非法出牌應回傳 False")
        self.assertEqual(len(player.hand.cards), initial_count,
                        "非法出牌後手牌應不變")
    
    def test_pass_increments_counter(self):
        """【測試9】過牌計數增加
        
        給定：玩家過牌
        預期：pass_count 增加 1
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        initial_pass = game.pass_count
        
        # 【執行】
        game.pass_turn()
        
        # 【驗證】
        self.assertEqual(game.pass_count, initial_pass + 1,
                        "過牌後計數應增加1")


class TestTurnManagement(unittest.TestCase):
    """測試回合管理 (BigTwoGame.next_turn)
    
    驗證：
    1. 3人過牌後重置
    2. 回合輪轉
    """
    
    def test_three_passes_resets(self):
        """【測試10】3人過牌後重置 last_play
        
        給定：出牌後，3位玩家依次過牌
        預期：last_play 被重置為 None
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        player = game.get_current_player()
        card_to_play = Card(3, Suit.CLUB.value)
        
        # 【執行】首位玩家出牌
        game.play([card_to_play])
        self.assertIsNotNone(game.last_play, "出牌後 last_play 應有值")
        
        # 3人過牌
        for i in range(3):
            game.pass_turn()
        
        # 【驗證】
        self.assertIsNone(game.last_play, "3人過牌後 last_play 應重置")
        self.assertEqual(game.pass_count, 0, "過牌計數應重置")
    
    def test_turn_rotates(self):
        """【測試11】回合輪轉到下家
        
        給定：執行 next_turn()
        預期：當前玩家索引增加
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        initial_idx = game.current_player_idx
        
        # 【執行】
        game.next_turn()
        
        # 【驗證】
        expected_idx = (initial_idx + 1) % 4
        self.assertEqual(game.current_player_idx, expected_idx,
                        "應輪轉到下家")


class TestWinCondition(unittest.TestCase):
    """測試獲勝條件 (BigTwoGame._check_winner 和 get_winner)
    
    驗證：
    1. 手牌空時遊戲結束
    2. 獲勝者被正確識別
    3. 遊戲未結束時無獲勝者
    """
    
    def test_detect_winner(self):
        """【測試12】手牌全部出完時有獲勝者
        
        給定：玩家手牌全部出完
        預期：get_winner() 回傳該玩家
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        player = game.get_current_player()
        
        # 【執行】移除玩家的所有牌（模擬全部出完）
        cards_to_remove = player.hand.cards.copy()
        for card in cards_to_remove:
            player.hand.cards.remove(card)
        
        # 檢查獲勝者
        game._check_winner()
        winner = game.get_winner()
        
        # 【驗證】
        self.assertEqual(winner, player, "手牌空的玩家應為獲勝者")
    
    def test_no_winner_yet(self):
        """【測試13】遊戲中無獲勝者
        
        給定：遊戲進行中，有玩家還有牌
        預期：get_winner() 回傳 None
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 驗證至少有一位玩家有牌
        has_cards = any(len(p.hand.cards) > 0 for p in game.players)
        self.assertTrue(has_cards, "設置應正確")
        
        # 【驗證】
        self.assertIsNone(game.get_winner(), "進行中的遊戲無獲勝者")
    
    def test_game_ends(self):
        """【測試14】獲勝者出現時遊戲結束
        
        給定：有玩家手牌空
        預期：is_game_over = True
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        player = game.get_current_player()
        
        # 【執行】移除玩家的所有牌
        cards_to_remove = player.hand.cards.copy()
        for card in cards_to_remove:
            player.hand.cards.remove(card)
        
        # 檢查遊戲狀態
        game._check_winner()
        
        # 【驗證】
        self.assertTrue(game.is_game_over, "有獲勝者時遊戲應結束")


class TestGameStatus(unittest.TestCase):
    """測試遊戲狀態 (BigTwoGame.get_game_status)
    
    驗證：
    1. 狀態字典包含所需資訊
    2. 玩家牌數正確
    3. 當前玩家正確
    """
    
    def test_game_status_structure(self):
        """【測試15】遊戲狀態字典結構正確
        
        給定：遊戲初始化後
        預期：狀態字典包含所有必要欄位
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【執行】
        status = game.get_game_status()
        
        # 【驗證】
        required_keys = {
            'is_game_over', 'current_player', 'winner',
            'players_cards', 'last_play', 'pass_count'
        }
        self.assertTrue(required_keys.issubset(status.keys()),
                       "狀態字典應包含所有必要欄位")
    
    def test_game_status_accurate(self):
        """【測試16】遊戲狀態數據準確
        
        給定：遊戲進行中
        預期：狀態中的牌數、玩家等資訊符合實際
        """
        # 【準備】
        game = BigTwoGame("玩家1")
        
        # 【執行】
        status = game.get_game_status()
        
        # 【驗證】
        self.assertFalse(status['is_game_over'], "新遊戲不應結束")
        self.assertEqual(status['pass_count'], 0, "初始過牌計數應為0")
        self.assertEqual(len(status['players_cards']), 4, "應有4位玩家")


# ==================== 測試入口 ====================

if __name__ == '__main__':
    # 設定詳細的測試輸出格式
    unittest.main(verbosity=2)
