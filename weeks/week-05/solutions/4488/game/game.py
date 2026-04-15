"""Phase 5: Game flow control."""

from typing import List, Optional, Tuple
from game.models import Card, Deck, Hand, Player
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy


class BigTwoGame:
    """Big Two 遊戲主控制。"""

    def __init__(self) -> None:
        """初始化遊戲。"""
        self.deck = Deck()
        self.players: List[Player] = []
        self.current_player = 0
        self.last_play: Optional[List[Card]] = None
        self.last_player_name: Optional[str] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 0

    def setup(self) -> None:
        """設置並初始化遊戲。"""
        # 建立4位玩家 (1人3AI)
        self.players = [
            Player("Player", is_ai=False),
            Player("AI_1", is_ai=True),
            Player("AI_2", is_ai=True),
            Player("AI_3", is_ai=True),
        ]

        # 洗牌
        self.deck.shuffle()

        # 發13張牌給每位玩家
        for player in self.players:
            player.take_cards(self.deck.deal(13))
            player.hand.sort_desc()

        # 找3♣決定先手
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs() is not None:
                self.current_player = i
                break

        self.round_number = 1

    def play(self, player: Player, cards: List[Card]) -> bool:
        """執行出牌。
        
        Args:
            player: 出牌玩家
            cards: 出牌牌組
            
        Returns:
            是否成功出牌
        """
        if not self._is_valid_play(cards):
            return False

        # 移除手牌
        player.play_cards(cards)

        # 設定last_play
        self.last_play = cards
        self.last_player_name = player.name

        # 重置pass計數
        self.pass_count = 0

        # 檢查獲勝
        if len(player.hand) == 0:
            self.winner = player

        return True

    def pass_(self, player: Player) -> bool:
        """執行過牌。
        
        Args:
            player: 過牌玩家
            
        Returns:
            是否成功過牌
        """
        self.pass_count += 1

        # 3人過牌後重置
        if self.pass_count >= 3:
            self.last_play = None
            self.last_player_name = None
            self.pass_count = 0

        return True

    def next_turn(self) -> None:
        """輪到下一位玩家。"""
        self.current_player = (self.current_player + 1) % 4

    def _is_valid_play(self, cards: List[Card]) -> bool:
        """檢查是否為合法出牌。
        
        Args:
            cards: 要檢查的牌組
            
        Returns:
            是否合法
        """
        return HandClassifier.can_play(self.last_play, cards)

    def check_winner(self) -> Optional[Player]:
        """檢查是否有獲勝者。
        
        Returns:
            獲勝者或 None
        """
        for player in self.players:
            if len(player.hand) == 0:
                return player
        return None

    def is_game_over(self) -> bool:
        """遊戲是否結束。
        
        Returns:
            是否結束
        """
        return self.winner is not None

    def get_current_player(self) -> Player:
        """取得當前玩家。
        
        Returns:
            當前玩家
        """
        return self.players[self.current_player]

    def ai_turn(self) -> bool:
        """執行 AI 回合。
        
        Returns:
            是否出牌（True 出牌, False 過牌）
        """
        player = self.get_current_player()
        is_first = self.last_play is None

        valid_plays = HandFinder.get_all_valid_plays(player.hand, self.last_play)

        if not valid_plays:
            # 無合法出牌，過牌
            self.pass_(player)
            return False

        best_play = AIStrategy.select_best(valid_plays, player.hand, is_first)

        if best_play is None:
            # 無法出牌，過牌
            self.pass_(player)
            return False

        # 出牌
        self.play(player, best_play)
        return True

    def get_valid_plays_for_human(self) -> List[List[Card]]:
        """取得人類玩家的所有合法出牌。
        
        Returns:
            合法出牌清單
        """
        player = self.get_current_player()
        return HandFinder.get_all_valid_plays(player.hand, self.last_play)
