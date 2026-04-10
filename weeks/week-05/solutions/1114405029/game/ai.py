from typing import List, Optional
from .models import Card
from .classifier import HandClassifier, CardType
from .finder import HandFinder

class AIStrategy:
    """
    [P4] 具備大局觀的決策引擎
    包含拆牌懲罰、控場讓牌與聽牌衝刺邏輯
    """
    @staticmethod
    def select_best_move(hand: List[Card], last_play: Optional[List[Card]], must_include: Optional[Card] = None) -> Optional[List[Card]]:
        # 取得所有合法組合
        valid_moves = HandFinder.get_all_valid_plays(hand, last_play, must_include)
        
        # 如果沒有合法牌可出，只能 Pass
        if not valid_moves:
            return None 
            
        is_free_lead = (last_play is None)
        scored_moves = []
        
        # 針對每一種可能打分數
        for move in valid_moves:
            score = AIStrategy._evaluate_move(move, hand, is_free_lead)
            scored_moves.append((score, move))
            
        # 依分數由高至低排序
        scored_moves.sort(key=lambda x: x[0], reverse=True)
        best_score, best_move = scored_moves[0]
        
        # [智能 Pass 邏輯]
        # 如果不是必須出牌 (有上家)，且最好的一手牌分數極低 
        # (代表需要拆散大牌去壓小牌)，且手牌還很多 (>5張)，則選擇戰略性放棄
        if not is_free_lead and best_score < -150 and len(hand) > 5:
            return None
            
        return best_move

    @staticmethod
    def _evaluate_move(move: List[Card], hand: List[Card], is_free_lead: bool) -> float:
        info = HandClassifier.classify(move)
        if not info:
            return -9999
            
        m_type, m_rank, m_suit = info
        score = 0.0
        
        # 1. 出牌效率分 (保留大牌，清掉小牌)
        # m_rank 範圍 3~15 (15是數字2)
        if is_free_lead:
            score += (16 - m_rank) * 15  # 自由出牌：越小越想丟
        else:
            score += (16 - m_rank) * 5   # 接牌：用剛好能壓過去的牌就好
            
        # 2. 牌型加成 (傾向打出組合牌)
        type_bonus = {
            CardType.SINGLE: 0, 
            CardType.PAIR: 10, 
            CardType.TRIPLE: 20, 
            CardType.STRAIGHT: 40, 
            CardType.FLUSH: 50,
            CardType.FULL_HOUSE: 60,
            CardType.FOUR_OF_A_KIND: 100,
            CardType.STRAIGHT_FLUSH: 200
        }
        score += type_bonus.get(m_type, 0)
        
        # 3. 黑桃加成 (P4 規則：黑桃具備戰術價值)
        if any(c.suit == 3 for c in move):
            score += 5
        
        # 4. 拆牌懲罰 (避免 AI 變智障的核心)
        # 如果出的是單張，檢查這張牌在手牌中是否有同伴
        if len(move) == 1:
            count = sum(1 for c in hand if c.rank == move[0].rank)
            if count == 2: score -= 80   # 拆對子
            if count == 3: score -= 200  # 拆三條
            if count == 4: score -= 500  # 拆鐵支 (絕對禁止)
            
        # 5. 聽牌與脫手獎勵 (致命一擊)
        remaining = len(hand) - len(move)
        if remaining == 0: 
            score += 10000 # 能贏絕對出
        elif remaining <= 2: 
            score += 500   # 聽牌階段積極搶攻
        
        return score