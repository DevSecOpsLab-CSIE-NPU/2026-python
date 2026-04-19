from typing import List, Optional, Tuple
from .models import Deck, Player, Card
from .分類器 import HandClassifier
from .finder import HandFinder
from .ai import AIStrategy

class BigTwoGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.current_player = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 1
    
    def setup(self) -> None:
        # 建立4位玩家
        self.players = [Player(f"Player{i+1}", is_ai=(i > 0)) for i in range(4)]
        
        # 洗牌
        self.deck.shuffle()
        
        # 發13張牌
        for _ in range(13):
            for player in self.players:
                cards = self.deck.deal(1)
                player.take_cards(cards)
        
        # 排序手牌
        for player in self.players:
            player.hand.sort_desc()
        
        # 找3♣決定先手
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs():
                self.current_player = i
                break
        
        # 初始化狀態
        self.last_play = None
        self.pass_count = 0
        self.winner = None
    
    def play(self, player: Player, cards: List[Card]) -> bool:
        # 出牌
        if not self._is_valid_play(cards):
            return False
        
        # 移除手牌
        player.play_cards(cards)
        
        # 設定last_play
        self.last_play = (cards, player.name)
        self.pass_count = 0
        
        # 檢查獲勝
        if len(player.hand) == 0:
            self.winner = player
        
        return True
    
    def pass_(self, player: Player) -> bool:
        # 過牌
        self.pass_count += 1
        return True
    
    def next_turn(self) -> None:
        # 下一位
        self.current_player = (self.current_player + 1) % 4
    
    def _is_valid_play(self, cards: List[Card]) -> bool:
        # 檢查合法性
        return HandClassifier.can_play(self.last_play[0] if self.last_play else None, cards)
    
    def check_round_reset(self) -> None:
        # pass_count >=3 時重置
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1
    
    def check_winner(self) -> Optional[Player]:
        # 檢查獲勝
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None
    
    def is_game_over(self) -> bool:
        # 遊戲結束
        return self.winner is not None
    
    def get_current_player(self) -> Player:
        # 當前玩家
        return self.players[self.current_player]
    
    def ai_turn(self) -> bool:
        # AI回合
        player = self.get_current_player()
        valid_plays = HandFinder.get_all_valid_plays(player.hand, self.last_play[0] if self.last_play else None)
        best_play = AIStrategy.select_best(valid_plays, player.hand, self.last_play is None)
        
        if best_play:
            return self.play(player, best_play)
        else:
            return self.pass_(player)