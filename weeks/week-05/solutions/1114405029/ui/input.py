from __future__ import annotations

from typing import Dict, List, Optional

import pygame

from p1_models import Card


class InputHandler:
	"""大老二 GUI 的輸入控制器。

	主要職責：
	1. 管理玩家目前選到的手牌索引（selected_indices）
	2. 處理滑鼠點擊（選牌、按鈕）
	3. 處理鍵盤快捷鍵（Enter 出牌、P 過牌）
	4. 將輸入動作轉成遊戲邏輯呼叫（game.play / game.pass_）
	"""

	# 與新版 Renderer.draw_hand 完全同步：牌寬 80、高 120、重疊間距 52。
	CARD_WIDTH = 80
	CARD_HEIGHT = 120
	HAND_SPACING = 52

	def __init__(
		self,
		hand_x: int = 80,
		hand_y: int = 500,
		buttons: Optional[Dict[str, pygame.Rect]] = None,
	) -> None:
		"""初始化輸入控制器。

		參數：
		- hand_x, hand_y：玩家手牌繪製起點，用來計算點擊對應的牌索引。
		- buttons：按鈕區域字典，格式例如：
		  {
			"play": pygame.Rect(...),
			"pass": pygame.Rect(...),
		  }
		"""
		# 儲存被選取的手牌索引，使用 list 方便與 UI 直接搭配。
		self.selected_indices: List[int] = []

		# 手牌區域定位（點擊座標轉索引需要）。
		self.hand_x = hand_x
		self.hand_y = hand_y

		# 操作按鈕（可在外部更新）。
		self.buttons: Dict[str, pygame.Rect] = buttons or {}

	def _toggle_index(self, index: int) -> None:
		"""切換指定牌索引的選取狀態（toggle）。"""
		if index in self.selected_indices:
			self.selected_indices.remove(index)
		else:
			self.selected_indices.append(index)

	def _get_clicked_card_index(self, pos: tuple[int, int], hand_count: int) -> Optional[int]:
		"""根據滑鼠座標計算點到哪一張手牌。

		由於手牌是重疊顯示，若點擊到重疊區，應以「最上層」（索引較大）牌為準。

		參數：
		- pos：滑鼠點擊座標
		- hand_count：目前手牌張數

		回傳：
		- 命中的牌索引（int）
		- 若未點到任何牌，回傳 None
		"""
		mouse_x, mouse_y = pos

		# 垂直範圍不在手牌區，直接視為未命中。
		if not (self.hand_y <= mouse_y <= self.hand_y + self.CARD_HEIGHT):
			return None

		# 從右到左檢查，確保重疊時優先命中最上層牌。
		for i in range(hand_count - 1, -1, -1):
			card_x = self.hand_x + i * self.HAND_SPACING
			if card_x <= mouse_x <= card_x + self.CARD_WIDTH:
				return i
		return None

	def handle_event(self, event: pygame.event.Event, game) -> bool:
		"""處理單一 pygame 事件。

		支援：
		- 滑鼠左鍵點擊：選牌/按鈕
		- 鍵盤：Enter（出牌）、P（過牌）

		回傳：
		- True：有觸發遊戲動作（例如出牌成功、過牌）
		- False：僅選牌或未處理事件
		"""
		if event.type == pygame.MOUSEBUTTONDOWN and getattr(event, "button", None) == 1:
			return self.handle_click(event.pos, game)

		if event.type == pygame.KEYDOWN:
			return self.handle_key(event.key, game)

		return False

	def handle_click(self, pos: tuple[int, int], game) -> bool:
		"""處理滑鼠點擊。

		處理順序：
		1. 先判斷是否點到按鈕（play/pass）
		2. 若不是按鈕，再判斷是否點到玩家手牌（toggle 選取）

		回傳：
		- True：觸發了出牌或過牌
		- False：僅切換選牌或無操作
		"""
		# 先處理按鈕點擊。
		play_rect = self.buttons.get("play")
		if play_rect and play_rect.collidepoint(pos):
			return self.try_play(game)

		pass_rect = self.buttons.get("pass")
		if pass_rect and pass_rect.collidepoint(pos):
			# 過牌規則分三種情況：
			# 情況 1：遊戲第一手（is_first_turn=True）→ 不可過牌，必須出 ♣3
			if game.is_first_turn:
				return False
			# 情況 2：非第一手但 last_play 為 None → 新回合起手
			#         起手者必須出牌，不允許直接 pass
			if game.last_play is None:
				return False
			# 情況 3：跟牌回合進行中（last_play 有值）→ 允許過牌
			current_player = game.get_current_player()
			game.pass_(current_player)
			self.selected_indices.clear()
			return True

		# 按鈕沒命中，改判斷是否點到手牌。
		current_player = game.get_current_player()
		index = self._get_clicked_card_index(pos, len(current_player.hand))
		if index is not None:
			self._toggle_index(index)

		return False

	def handle_key(self, key: int, game) -> bool:
		"""處理鍵盤快捷鍵。

		- Enter / Keypad Enter：嘗試出牌
		- P：過牌
		"""
		if key in (pygame.K_RETURN, pygame.K_KP_ENTER):
			return self.try_play(game)

		if key == pygame.K_p:
			# 過牌規則分三種情況：
			# 情況 1：遊戲第一手（is_first_turn=True）→ 不可過牌，必須出 ♣3
			if game.is_first_turn:
				return False
			# 情況 2：非第一手但 last_play 為 None → 新回合起手
			#         起手者必須出牌，不允許直接 pass
			if game.last_play is None:
				return False
			# 情況 3：跟牌回合進行中（last_play 有值）→ 允許過牌
			current_player = game.get_current_player()
			game.pass_(current_player)
			self.selected_indices.clear()
			return True

		return False

	def try_play(self, game) -> bool:
		"""嘗試將目前選取的牌送出。

		規則：
		1. 若沒有選牌，直接回傳 False
		2. 依 selected_indices 組成 cards 清單
		3. 呼叫 game.play(current_player, cards)
		4. 若成功，清空 selected_indices 並回傳 True
		5. 若失敗，保留選取狀態並回傳 False
		"""
		if not self.selected_indices:
			return False

		current_player = game.get_current_player()

		# 依索引排序，讓出牌順序穩定可預期。
		sorted_indices = sorted(set(self.selected_indices))

		# 防呆：索引若超出手牌範圍，視為無效輸入。
		if sorted_indices[-1] >= len(current_player.hand):
			return False

		cards = [current_player.hand[i] for i in sorted_indices]

		success = game.play(current_player, cards)
		if success:
			self.selected_indices.clear()
			return True

		return False
