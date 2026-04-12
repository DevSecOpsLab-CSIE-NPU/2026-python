from __future__ import annotations

import argparse
import math
import random
from array import array
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pygame


WIDTH, HEIGHT = 1180, 760
FPS = 60

BG = (18, 24, 32)
TOP_BG = (34, 44, 58)
LEFT_BG = (15, 20, 28)
RIGHT_BG = (244, 247, 250)
TEXT_LIGHT = (236, 242, 248)
TEXT_DARK = (22, 30, 40)
ACCENT = (255, 217, 102)
BAR_BG = (62, 76, 92)
BAR_FG = (77, 134, 255)
BAR_DEAD = (130, 130, 130)
DESC_TEXT = (245, 236, 214)
ERROR_TEXT = (255, 152, 152)

SCROLL_GOLD = (188, 144, 68)
SCROLL_GOLD_LIGHT = (228, 196, 126)
SCROLL_GOLD_DARK = (94, 64, 28)


def draw_scroll_frame(
    surface: pygame.Surface,
    rect: pygame.Rect,
    fill: Tuple[int, int, int, int] | Tuple[int, int, int],
    border_main: Tuple[int, int, int, int] | Tuple[int, int, int],
    border_inner: Tuple[int, int, int, int] | Tuple[int, int, int],
    ornament: Tuple[int, int, int, int] | Tuple[int, int, int],
    radius: int = 10,
) -> None:
    def _rgb(color: Tuple[int, ...]) -> Tuple[int, int, int]:
        return (color[0], color[1], color[2])

    def _rgba(color: Tuple[int, ...], alpha: int) -> Tuple[int, int, int, int]:
        r, g, b = _rgb(color)
        return (r, g, b, alpha)

    pygame.draw.rect(surface, fill, rect, border_radius=radius)
    pygame.draw.rect(surface, _rgba(SCROLL_GOLD_DARK, 120), rect, width=1, border_radius=radius)
    pygame.draw.rect(surface, border_main, rect, width=2, border_radius=radius)

    # Aged bevel: brighter on top/left and darker on bottom/right for a retro engraved feel.
    inset_1 = rect.inflate(-2, -2)
    if inset_1.width > 0 and inset_1.height > 0:
        pygame.draw.line(surface, _rgba(SCROLL_GOLD_LIGHT, 100), inset_1.topleft, inset_1.topright, 1)
        pygame.draw.line(surface, _rgba(SCROLL_GOLD_LIGHT, 90), inset_1.topleft, inset_1.bottomleft, 1)
        pygame.draw.line(surface, _rgba(SCROLL_GOLD_DARK, 120), inset_1.bottomleft, inset_1.bottomright, 1)
        pygame.draw.line(surface, _rgba(SCROLL_GOLD_DARK, 110), inset_1.topright, inset_1.bottomright, 1)

    inner = rect.inflate(-6, -6)
    if inner.width > 0 and inner.height > 0:
        pygame.draw.rect(surface, border_inner, inner, width=1, border_radius=max(4, radius - 3))
    inner_2 = rect.inflate(-10, -10)
    if inner_2.width > 0 and inner_2.height > 0:
        pygame.draw.rect(surface, _rgba(border_inner, 90), inner_2, width=1, border_radius=max(3, radius - 5))

    corner_len = max(6, min(14, rect.width // 5, rect.height // 2))
    x1, y1 = rect.left + 4, rect.top + 4
    x2, y2 = rect.right - 5, rect.bottom - 5
    pygame.draw.line(surface, ornament, (x1, y1), (x1 + corner_len, y1), 2)
    pygame.draw.line(surface, ornament, (x1, y1), (x1, y1 + corner_len), 2)
    pygame.draw.line(surface, ornament, (x2, y1), (x2 - corner_len, y1), 2)
    pygame.draw.line(surface, ornament, (x2, y1), (x2, y1 + corner_len), 2)
    pygame.draw.line(surface, ornament, (x1, y2), (x1 + corner_len, y2), 2)
    pygame.draw.line(surface, ornament, (x1, y2), (x1, y2 - corner_len), 2)
    pygame.draw.line(surface, ornament, (x2, y2), (x2 - corner_len, y2), 2)
    pygame.draw.line(surface, ornament, (x2, y2), (x2, y2 - corner_len), 2)

    if rect.height >= 24:
        left_mid = (rect.left + 4, rect.centery)
        right_mid = (rect.right - 5, rect.centery)
        pygame.draw.rect(surface, _rgba(ornament, 210), pygame.Rect(left_mid[0] - 1, left_mid[1] - 3, 3, 6), border_radius=1)
        pygame.draw.rect(surface, _rgba(ornament, 210), pygame.Rect(right_mid[0] - 1, right_mid[1] - 3, 3, 6), border_radius=1)

    if rect.width >= 120:
        cx = rect.centerx
        pygame.draw.line(surface, _rgba(border_main, 110), (cx - 24, rect.top + 2), (cx + 24, rect.top + 2), 1)
        pygame.draw.line(surface, _rgba(border_main, 100), (cx - 24, rect.bottom - 3), (cx + 24, rect.bottom - 3), 1)

SENSITIVE_KEYWORDS = [
    "幹",
    "操",
    "草",
    "老二",
    "雞雞",
    "鸡鸡",
    "鮑魚",
    "鲍鱼",
    "色情",
    "性愛",
    "性行為",
    "fuck",
    "fucker",
    "fucking",
    "bitch",
    "shit",
    "cao",
    "dick",
    "cock",
    "cocksmoker",
    "cocksucker",
    "penis",
    "pussy",
    "vagina",
    "vaginal",
    "clit",
    "clitoris",
    "tits",
    "sex",
    "porn",
    "nude",
    "xxx",
    "anal",
    "anus",
    "blowjob",
    "handjob",
    "cum",
    "cumslut",
    "masturbation",
    "masterbate",
    "orgasm",
    "erection",
    "g-spot",
    "gspot",
    "nazi",
]


@dataclass
class Unit:
    faction: str
    name: str
    hp: int
    atk: int
    def_: int
    spd: int
    is_leader: bool
    current_hp: int
    defense_mode: bool = False

    @property
    def alive(self) -> bool:
        return self.current_hp > 0


class Card:
    def __init__(self, name: str, card_type: str, damage_mult: float = 0.0, heal_mult: float = 0.0):
        self.name = name
        self.card_type = card_type
        self.damage_mult = damage_mult
        self.heal_mult = heal_mult

    def __repr__(self) -> str:
        return f"Card({self.name})"


class CardSystem:
    CARDS = [
        Card("攻擊", "attack", damage_mult=1.0),
        Card("防守", "defense", damage_mult=0.0),
        Card("恢復", "heal", damage_mult=0.0, heal_mult=0.5),
        Card("必殺", "ultimate", damage_mult=1.8),
    ]

    @staticmethod
    def get_cards() -> List[Card]:
        return CardSystem.CARDS


class Button:
    def __init__(self, rect: pygame.Rect, text: str):
        self.rect = rect
        self.text = text
        self.enabled = True

    def draw(self, surface: pygame.Surface, font: pygame.font.Font) -> None:
        hovered = self.enabled and self.rect.collidepoint(pygame.mouse.get_pos())
        fill = (176, 138, 72, 232) if hovered else ((102, 74, 34, 208) if self.enabled else (64, 58, 46, 135))
        border = (255, 236, 180, 250) if hovered else ((232, 194, 112, 228) if self.enabled else (126, 110, 82, 165))
        panel = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        draw_scroll_frame(
            panel,
            panel.get_rect(),
            fill,
            border,
            (184, 146, 82, 220) if self.enabled else (92, 84, 70, 150),
            (255, 244, 214, 240) if self.enabled else (136, 126, 106, 155),
            radius=8,
        )
        surface.blit(panel, self.rect.topleft)
        label_color = (255, 250, 232) if hovered else ((246, 230, 186) if self.enabled else (168, 160, 145))
        label = font.render(self.text, True, label_color)
        surface.blit(label, label.get_rect(center=self.rect.center))

    def hit(self, pos: Tuple[int, int]) -> bool:
        return self.enabled and self.rect.collidepoint(pos)


class ChibiBattlePygame:
    def __init__(self, generals_path: Path):
        self.generals_path = generals_path
        self.units: Dict[str, Unit] = {}
        self.turn_order: List[str] = []
        self.turn_index = 0
        self.current_attacker: Optional[str] = None
        self.auto_mode = False
        self.scene = "lobby"
        self.request_quit = False
        self.difficulty = "普通"
        self.player_name = ""
        self.name_error = ""
        self.name_input_active = False
        self.animation_enabled = True
        self.sound_enabled = True
        self.battle_sfx_enabled = True
        self.opening_anim_duration = 45
        self.opening_anim_timer = 0
        self.mixer_ready = False
        self.sfx_click: Optional[pygame.mixer.Sound] = None
        self.sfx_start: Optional[pygame.mixer.Sound] = None
        self.sfx_hurt: Optional[pygame.mixer.Sound] = None
        self.sfx_heal: Optional[pygame.mixer.Sound] = None
        self.sfx_defense: Optional[pygame.mixer.Sound] = None
        self.sfx_ultimate: Optional[pygame.mixer.Sound] = None
        self.lobby_background_image: Optional[pygame.Surface] = None
        self.battle_background_image: Optional[pygame.Surface] = None
        self._background_scaled: Optional[pygame.Surface] = None
        self._background_scaled_size: Optional[Tuple[int, int]] = None
        self._background_scaled_scene: Optional[str] = None

        self.log_lines: List[str] = []
        self.log_view_rect = pygame.Rect(0, 0, 0, 0)
        self.log_visible_lines = 8
        self.log_scroll_offset = 0
        self.start_countdown_msgs: List[str] = []
        self.start_countdown_index = 0
        self.start_countdown_next_tick = 0
        self.start_countdown_active = False
        self.initiative_spin_active = False
        self.initiative_spin_start_ms = 0
        self.initiative_spin_duration_ms = 0
        self.initiative_player_first = True
        self.initiative_spin_start_angle = 0.0
        self.initiative_spin_total_angle = 0.0
        self.initiative_spin_current_angle = 0.0
        self.initiative_result_pending_active = False
        self.initiative_result_pending_player_first = True
        self.initiative_result_pending_execute_ms = 0
        self.initiative_result_pending_delay_ms = 3000
        self.ai_pending_active = False
        self.ai_pending_attacker: Optional[str] = None
        self.ai_pending_execute_ms = 0
        self.ai_pending_delay_ms = 0
        self.targets: List[str] = []
        self.target_index = -1
        self.unit_card_rects: Dict[str, pygame.Rect] = {}
        self.awaiting_actor_selection = False
        self.awaiting_target_selection = False
        self.toast_text = ""
        self.toast_start_ms = 0
        self.toast_hold_ms = 1400
        self.toast_fade_ms = 600
        self.toast_default_hold_ms = 1400
        self.heal_cooldown_rounds = 4
        self.heal_team_cooldowns: Dict[str, int] = {"蜀吳": 0, "魏": 0}
        self.round_action_sides: Set[str] = set()
        self.ai_heal_uses_by_team: Dict[str, int] = {"蜀吳": 0, "魏": 0}
        self.ultimate_ready_notified_actor: Optional[str] = None
        self.game_over_active = False
        self.game_over_victory = False
        self.game_over_text = ""
        self.game_over_fireworks: List[Dict[str, float]] = []
        self.firework_last_spawn_ms = 0
        self.damage_floats: List[Dict[str, float | str]] = []
        
        self.card_selected: Optional[Card] = None
        self.available_cards = CardSystem.get_cards()
        self.player_faction = "蜀"
        self.offensive_cards = [c for c in self.available_cards if c.card_type in ["attack", "ultimate"]]
        self.support_cards = [c for c in self.available_cards if c.card_type in ["defense", "heal"]]

        self.btn_restart = Button(pygame.Rect(790, 55, 120, 34), "重新開始")
        self.btn_auto = Button(pygame.Rect(920, 55, 120, 34), "開始自動攻擊")
        self.btn_lobby = Button(pygame.Rect(650, 55, 130, 34), "返回大廳")

        self.btn_attack = Button(pygame.Rect(800, 255, 330, 38), "確認使用")
        self.btn_target_prev = Button(pygame.Rect(800, 205, 34, 34), "<")
        self.btn_target_next = Button(pygame.Rect(1096, 205, 34, 34), ">")
        self.btn_end_restart = Button(pygame.Rect(0, 0, 210, 56), "重新開始")
        self.btn_end_lobby = Button(pygame.Rect(0, 0, 210, 56), "返回大廳")

        self.btn_start_game = Button(pygame.Rect(420, 440, 340, 56), "進入赤壁戰場")
        self.btn_lobby_help = Button(pygame.Rect(420, 512, 340, 50), "遊戲說明")
        self.btn_lobby_quit = Button(pygame.Rect(420, 512, 340, 50), "離開遊戲")
        self.btn_diff_easy = Button(pygame.Rect(260, 340, 150, 42), "簡單")
        self.btn_diff_normal = Button(pygame.Rect(455, 340, 150, 42), "普通")
        self.btn_diff_hard = Button(pygame.Rect(650, 340, 150, 42), "困難")
        self.btn_diff_continue = Button(pygame.Rect(420, 512, 340, 56), "下一步")
        self.btn_diff_back = Button(pygame.Rect(420, 578, 340, 50), "返回大廳")
        self.btn_toggle_battle_sfx = Button(pygame.Rect(260, 410, 260, 42), "對局音效：開")
        self.btn_toggle_sound = Button(pygame.Rect(540, 410, 260, 42), "按鍵音效：開")
        self.name_box = pygame.Rect(330, 236, 520, 44)
        self.name_entry_box = pygame.Rect(284, 368, 612, 56)
        self.lobby_help_active = False

        self.turn_info = "回合資訊：等待開始"
        self.show_lobby()

    def _resolve_generals_path(self) -> Path:
        current_dir = Path(__file__).resolve().parent
        search_roots = [current_dir, current_dir.parent, current_dir.parent.parent]
        candidate_names = ["generals.txt", "角色資料主檔.txt"]

        for root in search_roots:
            for name in candidate_names:
                path = root / name
                if path.exists() and path.is_file():
                    return path

        if self.generals_path.exists() and self.generals_path.is_file():
            return self.generals_path
        return self.generals_path

    def _difficulty_factors(self, faction: str) -> Tuple[float, float, float, float]:
        # Rebalance: all difficulties are weaker than source data, and HP drops more to shorten battle length.
        allied = faction in ["蜀", "吳"]
        if self.difficulty == "困難":
            return (0.78, 0.90, 0.84, 0.95) if allied else (0.84, 0.95, 0.88, 0.98)
        if self.difficulty == "普通":
            return (0.72, 0.86, 0.80, 0.93) if allied else (0.81, 0.93, 0.87, 0.96)
        return (0.68, 0.84, 0.76, 0.92) if allied else (0.62, 0.78, 0.72, 0.90)

    def _scale_stat(self, value: int, factor: float) -> int:
        return max(1, int(round(value * factor)))

    def load_generals(self) -> Dict[str, Unit]:
        units: Dict[str, Unit] = {}
        with self._resolve_generals_path().open("r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                if line == "EOF":
                    break
                faction, name, hp, atk, def_, spd, is_leader = line.split()
                hp_factor, atk_factor, def_factor, spd_factor = self._difficulty_factors(faction)
                hp_i = self._scale_stat(int(hp), hp_factor)
                if name == "夏侯惇":
                    if self.difficulty == "簡單":
                        hp_i = 80
                    elif self.difficulty == "普通":
                        hp_i = 95
                    else:
                        hp_i = 100
                units[name] = Unit(
                    faction=faction,
                    name=name,
                    hp=hp_i,
                    atk=self._scale_stat(int(atk), atk_factor),
                    def_=self._scale_stat(int(def_), def_factor),
                    spd=self._scale_stat(int(spd), spd_factor),
                    is_leader=(is_leader == "True"),
                    current_hp=hp_i,
                )
        return units

    def load_new_game(self) -> None:
        self.units = self.load_generals()
        self.heal_team_cooldowns = {"蜀吳": 0, "魏": 0}
        self.round_action_sides = set()
        self.ai_heal_uses_by_team = {"蜀吳": 0, "魏": 0}
        self.turn_order = self._alive_sorted_names()
        self.turn_index = 0
        self.current_attacker = None
        self.auto_mode = False
        self.game_over_active = False
        self.game_over_victory = False
        self.game_over_text = ""
        self.game_over_fireworks = []
        self.firework_last_spawn_ms = 0
        self.damage_floats = []
        self.targets = []
        self.target_index = -1
        self.turn_info = "回合資訊：新遊戲已開始，請先選擇角色"
        pname = self.player_name.strip() or "主公"
        self.log_lines = [
            f"=== 赤壁之戰開始｜玩家：{pname} ===",
            f"難度：{self.difficulty}",
            "【戰場】江面烽火四起，三軍列陣待發！",
        ]
        self.log_scroll_offset = 0
        self.start_countdown_msgs = []
        self.start_countdown_index = 0
        self.start_countdown_next_tick = 0
        self.start_countdown_active = False
        self.initiative_result_pending_active = False
        self.initiative_result_pending_player_first = True
        self.initiative_result_pending_execute_ms = 0
        self.initiative_result_pending_delay_ms = 3000
        self.initiative_spin_active = False
        self.initiative_spin_start_ms = 0
        self.initiative_spin_duration_ms = 0
        self.initiative_player_first = True
        self.initiative_spin_start_angle = 0.0
        self.initiative_spin_total_angle = 0.0
        self.initiative_spin_current_angle = 0.0
        self.ai_pending_active = False
        self.ai_pending_attacker = None
        self.ai_pending_execute_ms = 0
        self.ai_pending_delay_ms = 0
        self.awaiting_actor_selection = False
        self.awaiting_target_selection = False
        self.toast_text = ""
        self.toast_start_ms = 0
        self.ultimate_ready_notified_actor = None
        self.btn_auto.text = "開始自動攻擊"
        self.btn_attack.enabled = False
        self.btn_target_prev.enabled = False
        self.btn_target_next.enabled = False

    def show_lobby(self) -> None:
        self.scene = "lobby"
        self.auto_mode = False
        self.lobby_help_active = False
        self.name_input_active = False
        self.name_error = ""
        pygame.key.stop_text_input()
        self.turn_info = "回合資訊：等待開始"
        self.btn_start_game.rect = pygame.Rect(420, 456, 340, 56)
        self.btn_lobby_help.rect = pygame.Rect(420, 526, 340, 50)
        self.btn_lobby_quit.rect = pygame.Rect(420, 590, 340, 50)
        self.btn_start_game.text = "進入遊戲設定"
        self.btn_lobby_help.text = "遊戲說明"
        self.btn_lobby_quit.text = "離開遊戲"
        self.btn_toggle_battle_sfx.text = f"對局音效：{'開' if self.battle_sfx_enabled else '關'}"
        self.btn_toggle_sound.text = f"按鍵音效：{'開' if self.sound_enabled else '關'}"

    def start_game(self) -> None:
        self.scene = "difficulty"

    def start_name_entry(self) -> None:
        self.scene = "name_entry"
        self.name_input_active = True
        self.name_error = ""
        self.btn_lobby_quit.text = "返回難度"
        self.name_entry_box = pygame.Rect(284, 388, 612, 56)
        pygame.key.start_text_input()
        pygame.key.set_text_input_rect(self.name_entry_box)

    @staticmethod
    def _normalize_for_sensitive_check(text: str) -> str:
        lowered = text.casefold()
        return "".join(ch for ch in lowered if ch.isalnum() or ("\u4e00" <= ch <= "\u9fff"))

    def _contains_sensitive_word(self, text: str) -> bool:
        normalized = self._normalize_for_sensitive_check(text)
        return any(keyword in normalized for keyword in SENSITIVE_KEYWORDS)

    def _start_battle_with_initiative(self) -> None:
        self.load_new_game()
        self.scene = "battle"
        self.opening_anim_timer = self.opening_anim_duration if self.animation_enabled else 0
        if not self.animation_enabled:
            player_first = random.choice([True, False])
            first_side = "玩家" if player_first else "AI"
            self._append_log(f"【系統】轉盤結果：{first_side}先攻")
            self._set_turn_order_by_side(player_first=player_first)
            if player_first:
                self._enter_actor_selection_phase(show_prompt=False)
            else:
                self.next_turn()
            return

        self.start_countdown_msgs = [
            "【系統】倒數 5",
            "【系統】倒數 4",
            "【系統】倒數 3",
            "【系統】倒數 2",
            "【系統】倒數 1",
            "【系統】遊戲開始！",
        ]
        self.start_countdown_index = 0
        self.start_countdown_next_tick = 0
        self.start_countdown_active = False
        self.turn_info = "回合資訊：轉盤決定先攻中..."
        self._start_initiative_spin()
        self._play_sfx("start")

    def confirm_name_and_start(self) -> None:
        entered = self.player_name.strip() or "主公"
        if self._contains_sensitive_word(entered):
            self.name_error = "暱稱含敏感字詞，請更換後再開始遊戲。"
            self.name_input_active = True
            return

        self.name_error = ""
        self.player_name = entered
        self.name_input_active = False
        pygame.key.stop_text_input()
        self._start_battle_with_initiative()

    def _clear_in_game_progress(self) -> None:
        # Ensure returning to lobby always discards the running match state immediately.
        self.units = {}
        self.turn_order = []
        self.turn_index = 0
        self.current_attacker = None
        self.card_selected = None
        self.auto_mode = False
        self.targets = []
        self.target_index = -1
        self.unit_card_rects = {}
        self.awaiting_actor_selection = False
        self.awaiting_target_selection = False

        self.heal_team_cooldowns = {"蜀吳": 0, "魏": 0}
        self.round_action_sides = set()
        self.ai_heal_uses_by_team = {"蜀吳": 0, "魏": 0}
        self.ultimate_ready_notified_actor = None

        self.log_lines = []
        self.log_scroll_offset = 0
        self.turn_info = "回合資訊：等待開始"
        self.damage_floats = []

        self.start_countdown_msgs = []
        self.start_countdown_index = 0
        self.start_countdown_next_tick = 0
        self.start_countdown_active = False

        self.initiative_spin_active = False
        self.initiative_spin_start_ms = 0
        self.initiative_spin_duration_ms = 0
        self.initiative_player_first = True
        self.initiative_spin_start_angle = 0.0
        self.initiative_spin_total_angle = 0.0
        self.initiative_spin_current_angle = 0.0

        self.initiative_result_pending_active = False
        self.initiative_result_pending_player_first = True
        self.initiative_result_pending_execute_ms = 0

        self.ai_pending_active = False
        self.ai_pending_attacker = None
        self.ai_pending_execute_ms = 0
        self.ai_pending_delay_ms = 0

        self.toast_text = ""
        self.toast_start_ms = 0

        self.game_over_active = False
        self.game_over_victory = False
        self.game_over_text = ""
        self.game_over_fireworks = []
        self.firework_last_spawn_ms = 0

        self.btn_auto.text = "開始自動攻擊"
        self.btn_attack.enabled = False
        self.btn_target_prev.enabled = False
        self.btn_target_next.enabled = False

    def back_to_lobby(self) -> None:
        self._clear_in_game_progress()
        self.show_lobby()

    def set_sound_resources(
        self,
        mixer_ready: bool,
        click_sound: Optional[pygame.mixer.Sound],
        start_sound: Optional[pygame.mixer.Sound],
        hurt_sound: Optional[pygame.mixer.Sound],
        heal_sound: Optional[pygame.mixer.Sound],
        defense_sound: Optional[pygame.mixer.Sound],
        ultimate_sound: Optional[pygame.mixer.Sound],
    ) -> None:
        self.mixer_ready = mixer_ready
        self.sfx_click = click_sound
        self.sfx_start = start_sound
        self.sfx_hurt = hurt_sound
        self.sfx_heal = heal_sound
        self.sfx_defense = defense_sound
        self.sfx_ultimate = ultimate_sound

    def set_background_images(
        self,
        lobby_image: Optional[pygame.Surface],
        battle_image: Optional[pygame.Surface],
    ) -> None:
        self.lobby_background_image = lobby_image
        self.battle_background_image = battle_image
        self._background_scaled = None
        self._background_scaled_size = None
        self._background_scaled_scene = None

    def set_background_image(self, image: Optional[pygame.Surface]) -> None:
        self.set_background_images(image, image)

    def draw_background(self, surface: pygame.Surface, dim_alpha: int = 120, scene_type: str = "lobby") -> None:
        if scene_type == "battle":
            bg_image = self.battle_background_image or self.lobby_background_image
        else:
            bg_image = self.lobby_background_image or self.battle_background_image

        if bg_image is None:
            surface.fill(BG)
            return

        size = surface.get_size()
        if (
            self._background_scaled is None
            or self._background_scaled_size != size
            or self._background_scaled_scene != scene_type
        ):
            self._background_scaled = pygame.transform.smoothscale(bg_image, size)
            self._background_scaled_size = size
            self._background_scaled_scene = scene_type

        surface.blit(self._background_scaled, (0, 0))
        overlay = pygame.Surface(size, pygame.SRCALPHA)
        overlay.fill((8, 12, 20, dim_alpha))
        surface.blit(overlay, (0, 0))

    def draw_translucent_card(self, surface: pygame.Surface, rect: pygame.Rect) -> None:
        panel = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        draw_scroll_frame(
            panel,
            panel.get_rect(),
            (24, 20, 14, 162),
            (220, 184, 102, 212),
            (146, 116, 62, 196),
            (248, 220, 146, 230),
            radius=16,
        )
        surface.blit(panel, rect.topleft)

    def _generate_character_card(
        self,
        fonts: Dict[str, pygame.font.Font],
        unit: Unit,
        faction_color: Tuple[int, int, int],
    ) -> pygame.Surface:
        card_w, card_h = 100, 120
        card = pygame.Surface((card_w, card_h), pygame.SRCALPHA)

        alive = unit.alive
        cloth_color = faction_color if alive else (82, 90, 100)

        bg_color = (*cloth_color, 186) if alive else (74, 70, 64, 156)
        border_main = (*SCROLL_GOLD_LIGHT, 238) if alive else (150, 142, 126, 185)
        border_inner = (*SCROLL_GOLD, 220) if alive else (112, 106, 94, 165)
        ornament = (*SCROLL_GOLD_LIGHT, 220) if alive else (132, 126, 112, 170)
        draw_scroll_frame(
            card,
            card.get_rect(),
            bg_color,
            border_main,
            border_inner,
            ornament,
            radius=12,
        )

        name_text = fonts["log"].render(unit.name, True, (248, 238, 214) if alive else (170, 172, 172))
        name_rect = name_text.get_rect(center=(card_w // 2, 14))
        card.blit(name_text, name_rect)

        hp_ratio = 0 if unit.hp == 0 else (unit.current_hp / unit.hp)
        hp_bar_rect = pygame.Rect(8, 34, card_w - 16, 16)
        pygame.draw.rect(card, (42, 36, 28), hp_bar_rect, border_radius=4)
        pygame.draw.rect(card, (184, 146, 82), hp_bar_rect, width=1, border_radius=4)
        fill_w = int((card_w - 16) * hp_ratio)
        if fill_w > 0:
            hp_fill = pygame.Rect(8, 34, fill_w, 16)
            hp_color = (100, 200, 100) if hp_ratio > 0.5 else ((255, 180, 60) if hp_ratio > 0.25 else (220, 80, 80))
            pygame.draw.rect(card, hp_color, hp_fill, border_radius=4)

        # Keep all numeric text at a consistent size across every character card.
        stat_font = fonts["log"]

        hp_txt = stat_font.render(f"{unit.current_hp}/{unit.hp}", True, (245, 248, 252))
        hp_txt_rect = hp_txt.get_rect(center=hp_bar_rect.center)
        card.blit(hp_txt, hp_txt_rect)

        stat_lines = [
            f"攻{unit.atk}",
            f"防{unit.def_}",
            f"速{unit.spd}",
        ]
        stat_y = 72
        for stat_line in stat_lines:
            stat_txt = stat_font.render(stat_line, True, (200, 210, 220) if alive else (130, 140, 150))
            stat_rect = stat_txt.get_rect(center=(card_w // 2, stat_y))
            card.blit(stat_txt, stat_rect)
            stat_y += 16

        return card

    def _play_sfx(self, kind: str) -> None:
        if not self.mixer_ready:
            return
        if kind == "click":
            if not self.sound_enabled:
                return
            snd = self.sfx_click
        else:
            if not self.battle_sfx_enabled:
                return
            if kind == "start":
                snd = self.sfx_start
            elif kind == "hurt":
                snd = self.sfx_hurt
            elif kind == "heal":
                snd = self.sfx_heal
            elif kind == "defense":
                snd = self.sfx_defense
            elif kind == "ultimate":
                snd = self.sfx_ultimate
            else:
                snd = None
        if snd:
            snd.play()

    def _draw_wrapped_text(
        self,
        surface: pygame.Surface,
        font: pygame.font.Font,
        text: str,
        color: Tuple[int, int, int],
        rect: pygame.Rect,
        max_lines: int = 3,
        line_spacing: int = 4,
    ) -> None:
        lines: List[str] = []
        current = ""
        for ch in text:
            candidate = current + ch
            if font.size(candidate)[0] <= rect.width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)

        y = rect.y
        line_h = font.get_height() + line_spacing
        for line in lines[:max_lines]:
            rendered = font.render(line, True, color)
            surface.blit(rendered, (rect.x, y))
            y += line_h

    def _draw_chibi_unit(
        self,
        surface: pygame.Surface,
        fonts: Dict[str, pygame.font.Font],
        unit: Unit,
        center: Tuple[int, int],
        faction_color: Tuple[int, int, int],
        show_target: bool,
        show_attacker: bool,
    ) -> pygame.Rect:
        cx, cy = center
        alive = unit.alive

        card = self._generate_character_card(fonts, unit, faction_color)
        card_rect = card.get_rect(center=(cx, cy))
        surface.blit(card, card_rect)

        if show_attacker:
            outline_color = (255, 224, 148)
            outline_width = 4
        elif show_target:
            outline_color = (250, 132, 124)
            outline_width = 3
        else:
            outline_color = (196, 160, 92) if alive else (132, 120, 98)
            outline_width = 2
        pygame.draw.rect(surface, outline_color, card_rect, outline_width, border_radius=12)
        return card_rect

    def _draw_chibi_battlefield(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        battlefield = pygame.Rect(16, 124, 744, 624)
        overlay = pygame.Surface((battlefield.width, battlefield.height), pygame.SRCALPHA)
        draw_scroll_frame(
            overlay,
            overlay.get_rect(),
            (12, 16, 24, 128),
            (214, 171, 86, 175),
            (142, 108, 52, 165),
            (248, 220, 146, 185),
            radius=14,
        )
        surface.blit(overlay, battlefield.topleft)

        rows = [
            ("蜀", (226, 104, 104), ["關羽", "劉備", "諸葛亮"]),
            ("吳", (84, 188, 130), ["周瑜", "孫權", "黃蓋"]),
            ("魏", (88, 152, 214), ["夏侯惇", "曹操", "郭嘉"]),
        ]
        row_y = [240, 408, 576]
        col_x = [180, 388, 596]
        self.unit_card_rects = {}

        current_target = self.targets[self.target_index] if (0 <= self.target_index < len(self.targets)) else ""
        for idx, (faction, color, names) in enumerate(rows):
            label = fonts["faction"].render(f"{faction}軍", True, color)
            surface.blit(label, (battlefield.x + 20, row_y[idx] - 84))

            pygame.draw.line(
                surface,
                (*color, 180),
                (battlefield.x + 88, row_y[idx] - 66),
                (battlefield.right - 28, row_y[idx] - 66),
                2,
            )

            for j, name in enumerate(names):
                unit = self.units.get(name)
                if unit is None:
                    continue
                center = (col_x[j], row_y[idx])
                card_rect = self._draw_chibi_unit(
                    surface,
                    fonts,
                    unit,
                    center,
                    color,
                    show_target=(unit.name == current_target),
                    show_attacker=(unit.name == self.current_attacker),
                )
                self.unit_card_rects[unit.name] = card_rect

    def _alive_sorted_names(self) -> List[str]:
        alive = [u for u in self.units.values() if u.alive]
        alive.sort(key=lambda u: (-u.spd, u.name))
        return [u.name for u in alive]

    def _alive_by_factions(self, factions: List[str]) -> List[str]:
        return [u.name for u in self.units.values() if u.faction in factions and u.alive]

    def _allied_factions(self, faction: str) -> List[str]:
        if faction in ["蜀", "吳"]:
            return ["蜀", "吳"]
        return ["魏"]

    def _enemy_factions(self, faction: str) -> List[str]:
        if faction in ["蜀", "吳"]:
            return ["魏"]
        return ["蜀", "吳"]

    def _team_key(self, faction: str) -> str:
        return "蜀吳" if faction in ["蜀", "吳"] else "魏"

    def _attackable_enemy_targets(self, attacker: Unit) -> List[str]:
        enemies = self._alive_by_factions(self._enemy_factions(attacker.faction))
        return [name for name in enemies if not self.units[name].defense_mode]

    def _targets_for_card(self, attacker: Unit, card: Optional[Card]) -> List[str]:
        if card and card.card_type in ["defense", "heal"]:
            return [attacker.name] if attacker.alive else []
        if card and card.card_type == "ultimate":
            return self._low_hp_enemy_targets(attacker, threshold=20)
        return self._attackable_enemy_targets(attacker)

    def _low_hp_enemy_targets(self, attacker: Unit, threshold: int = 20) -> List[str]:
        enemies = self._attackable_enemy_targets(attacker)
        return [name for name in enemies if self.units[name].current_hp <= threshold]

    def _is_card_enabled_for_actor(self, attacker: Unit, card: Card) -> bool:
        if card.card_type == "heal":
            cooldown_ready = self.heal_team_cooldowns.get(self._team_key(attacker.faction), 0) == 0
            return cooldown_ready and attacker.current_hp < attacker.hp
        if card.card_type == "ultimate":
            return len(self._low_hp_enemy_targets(attacker, threshold=20)) > 0
        return True

    def _tick_heal_cooldowns(self, exclude_team_key: Optional[str] = None) -> None:
        completed = False
        for team_key, remain in list(self.heal_team_cooldowns.items()):
            if exclude_team_key is not None and team_key == exclude_team_key:
                continue
            if remain <= 0:
                continue
            next_remain = remain - 1
            self.heal_team_cooldowns[team_key] = next_remain
            if next_remain == 0:
                completed = True
        if completed:
            self._show_toast("恢復已冷卻完成！")

    def _mark_valid_action_and_tick_round(self, attacker_faction: str, exclude_team_key: Optional[str] = None) -> None:
        self.round_action_sides.add(self._team_key(attacker_faction))
        if len(self.round_action_sides) < 2:
            return
        self.round_action_sides.clear()
        self._tick_heal_cooldowns(exclude_team_key=exclude_team_key)

    def _ai_heal_cap(self) -> int:
        if self.difficulty == "簡單":
            return 1
        if self.difficulty == "普通":
            return 2
        return 4

    def _can_ai_use_heal(self, attacker: Unit, heal_card: Card) -> bool:
        team_key = self._team_key(attacker.faction)
        return self._is_card_enabled_for_actor(attacker, heal_card) and self.ai_heal_uses_by_team.get(team_key, 0) < self._ai_heal_cap()

    def _refresh_targets_for_current_selection(self) -> None:
        if not self.current_attacker:
            self.targets = []
            self.target_index = -1
            self.btn_target_prev.enabled = False
            self.btn_target_next.enabled = False
            return

        attacker = self.units[self.current_attacker]
        self.targets = self._targets_for_card(attacker, self.card_selected)
        if self.card_selected and self.card_selected.card_type in ["defense", "heal"] and self.targets:
            self.target_index = 0
        elif not self.targets or not (0 <= self.target_index < len(self.targets)):
            self.target_index = -1
        self.btn_target_prev.enabled = len(self.targets) > 1
        self.btn_target_next.enabled = len(self.targets) > 1

    def _pick_ai_target(self, names: List[str]) -> str:
        return min(names, key=lambda n: (self.units[n].current_hp, n))

    def _calc_damage(self, attacker: Unit, defender: Unit, card: Card) -> int:
        if card.card_type == "defense":
            return 0
        base = max(1, attacker.atk - defender.def_)
        if defender.defense_mode:
            base = max(0, base - 5)
        damage = int(base * card.damage_mult)
        if attacker.is_leader:
            damage += 2
        return max(0, damage)

    def _calc_heal(self, unit: Unit, card: Card) -> int:
        if card.card_type != "heal":
            return 0
        if self.difficulty == "困難":
            return 30
        if self.difficulty == "普通":
            return 18
        return 10

    def _create_damage_float(self, target_name: str, damage: int) -> None:
        """Create a floating damage text that appears above the target and fades away."""
        if target_name not in self.unit_card_rects:
            return
        card_rect = self.unit_card_rects[target_name]
        center_x = card_rect.centerx
        center_y = card_rect.centery - 60
        
        self.damage_floats.append({
            "x": float(center_x),
            "y": float(center_y),
            "damage": damage,
            "age_ms": 0.0,
            "max_age_ms": 1000.0,
        })

    def _update_damage_floats(self, dt_ms: float) -> None:
        """Update all floating damage texts, removing expired ones."""
        alive_floats = []
        for dmg_float in self.damage_floats:
            dmg_float["age_ms"] += dt_ms
            if dmg_float["age_ms"] < dmg_float["max_age_ms"]:
                alive_floats.append(dmg_float)
        self.damage_floats = alive_floats

    def _draw_damage_floats(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        """Draw all active floating damage texts with fade-out effect."""
        for dmg_float in self.damage_floats:
            progress = dmg_float["age_ms"] / dmg_float["max_age_ms"]
            fade = max(0.0, 1.0 - progress)
            
            offset_y = int(progress * 60)
            draw_x = int(dmg_float["x"])
            draw_y = int(dmg_float["y"] - offset_y)
            
            alpha = int(255 * fade)
            damage_str = f"-{int(dmg_float['damage'])}"
            
            damage_text = fonts["h2"].render(damage_str, True, (255, 100, 100))
            damage_text.set_alpha(alpha)
            surface.blit(damage_text, damage_text.get_rect(center=(draw_x, draw_y)))

    def _clear_side_defense_modes(self, faction: str) -> None:
        side_factions = self._allied_factions(faction)
        for unit in self.units.values():
            if unit.faction in side_factions:
                unit.defense_mode = False

    def _append_log(self, msg: str) -> None:
        was_at_bottom = self.log_scroll_offset == 0
        self.log_lines.append(msg)
        if len(self.log_lines) > 20:
            self.log_lines = self.log_lines[-20:]
        if was_at_bottom:
            self.log_scroll_offset = 0
        else:
            max_offset = max(0, len(self.log_lines) - self.log_visible_lines)
            self.log_scroll_offset = min(self.log_scroll_offset, max_offset)

    def _is_startup_input_locked(self) -> bool:
        return (
            self.initiative_spin_active
            or self.initiative_result_pending_active
            or self.start_countdown_active
        )

    def handle_log_scroll(self, delta_y: int) -> None:
        if self.scene != "battle":
            return
        if self._is_startup_input_locked():
            return
        if not self.log_view_rect.collidepoint(pygame.mouse.get_pos()):
            return
        max_offset = max(0, len(self.log_lines) - self.log_visible_lines)
        if max_offset == 0:
            return
        if delta_y > 0:
            self.log_scroll_offset = min(max_offset, self.log_scroll_offset + 1)
        elif delta_y < 0:
            self.log_scroll_offset = max(0, self.log_scroll_offset - 1)

    def _update_start_countdown(self) -> None:
        if not self.start_countdown_active:
            return
        now = pygame.time.get_ticks()
        while self.start_countdown_active and now >= self.start_countdown_next_tick:
            if self.start_countdown_index >= len(self.start_countdown_msgs):
                self.start_countdown_active = False
                return
            self._append_log(self.start_countdown_msgs[self.start_countdown_index])
            self.start_countdown_index += 1
            self.start_countdown_next_tick += 1000
            if self.start_countdown_index >= len(self.start_countdown_msgs):
                self.start_countdown_active = False
                if self.initiative_result_pending_player_first:
                    self._set_turn_order_by_side(player_first=True)
                    self._enter_actor_selection_phase(show_prompt=False)
                else:
                    self._set_turn_order_by_side(player_first=False)
                    self.next_turn()
                return

    def _set_turn_order_by_side(self, player_first: bool) -> None:
        order = self._alive_sorted_names()
        if not order:
            self.turn_order = []
            self.turn_index = 0
            return
        if player_first:
            pred = lambda n: self.units[n].faction in ["蜀", "吳"]
        else:
            pred = lambda n: self.units[n].faction == "魏"

        pivot = 0
        for i, name in enumerate(order):
            if pred(name):
                pivot = i
                break
        self.turn_order = order[pivot:] + order[:pivot]
        self.turn_index = 0

    def _spin_points_to_player(self, angle: float) -> bool:
        # Wheel is drawn with 玩家 on upper half. We rotate wheel by -angle,
        # so pointer-at-top sees 玩家 when angle falls in top-half sectors.
        a = angle % 360.0
        return a < 90.0 or a >= 270.0

    def _start_initiative_spin(self) -> None:
        desired_player_first = random.choice([True, False])
        self.initiative_player_first = desired_player_first
        self.initiative_spin_active = True
        self.initiative_spin_start_ms = pygame.time.get_ticks()
        self.initiative_spin_start_angle = random.uniform(0.0, 360.0)

        # Land near the center of the matching half to avoid boundary ambiguity.
        target_center = 0.0 if desired_player_first else 180.0
        target_angle = (target_center + random.uniform(-28.0, 28.0)) % 360.0
        start_norm = self.initiative_spin_start_angle % 360.0
        landing_delta = (target_angle - start_norm) % 360.0

        self.initiative_spin_duration_ms = random.randint(6000, 8000)
        full_spins = random.randint(3, 4)
        self.initiative_spin_total_angle = full_spins * 360.0 + landing_delta
        self.initiative_spin_current_angle = self.initiative_spin_start_angle

    def _apply_initiative_result(self) -> None:
        # Use actual final wheel angle as source of truth so visual result and logic always match.
        self.initiative_player_first = self._spin_points_to_player(self.initiative_spin_current_angle)
        first_side = "玩家" if self.initiative_player_first else "AI"
        self._append_log(f"【系統】轉盤結果：{first_side}先攻")
        self._show_toast(f"【系統】{first_side}先攻！")
        self.initiative_result_pending_active = True
        self.initiative_result_pending_player_first = self.initiative_player_first
        self.initiative_result_pending_execute_ms = pygame.time.get_ticks() + self.initiative_result_pending_delay_ms

    def _update_initiative_result_pending(self) -> None:
        if not self.initiative_result_pending_active:
            return
        if pygame.time.get_ticks() < self.initiative_result_pending_execute_ms:
            return

        self.initiative_result_pending_active = False
        self.start_countdown_index = 0
        self.start_countdown_next_tick = pygame.time.get_ticks() + 1000
        self.start_countdown_active = True
        self.turn_info = "回合資訊：倒數開始..."

    def _update_initiative_spin(self) -> None:
        if not self.initiative_spin_active:
            return
        elapsed = pygame.time.get_ticks() - self.initiative_spin_start_ms
        progress = min(1.0, elapsed / max(1, self.initiative_spin_duration_ms))
        eased = 1.0 - pow(1.0 - progress, 3)
        self.initiative_spin_current_angle = self.initiative_spin_start_angle + self.initiative_spin_total_angle * eased
        if progress >= 1.0:
            self.initiative_spin_active = False
            self._apply_initiative_result()

    def _show_toast(self, text: str) -> None:
        self.toast_text = text
        self.toast_start_ms = pygame.time.get_ticks()

    def _show_toast_for_seconds(self, text: str, seconds: float) -> None:
        """Show a toast message for a specified duration in seconds."""
        self.toast_text = text
        self.toast_start_ms = pygame.time.get_ticks()
        self.toast_hold_ms = int(seconds * 1000)

    def _draw_toast(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        if not self.toast_text:
            return
        elapsed = pygame.time.get_ticks() - self.toast_start_ms
        full_duration = self.toast_hold_ms + self.toast_fade_ms
        if elapsed >= full_duration:
            self.toast_text = ""
            self.toast_hold_ms = self.toast_default_hold_ms
            return

        alpha = 220
        if elapsed > self.toast_hold_ms:
            fade_ratio = 1.0 - ((elapsed - self.toast_hold_ms) / max(1, self.toast_fade_ms))
            alpha = max(0, int(220 * fade_ratio))

        toast_rect = pygame.Rect((WIDTH - 520) // 2, 66, 520, 34)
        panel = pygame.Surface((toast_rect.width, toast_rect.height), pygame.SRCALPHA)
        draw_scroll_frame(
            panel,
            panel.get_rect(),
            (64, 50, 28, alpha),
            (228, 192, 106, alpha),
            (146, 116, 62, alpha),
            (248, 220, 146, alpha),
            radius=8,
        )
        surface.blit(panel, toast_rect.topleft)
        txt = fonts["small"].render(self.toast_text, True, (245, 236, 214))
        surface.blit(txt, txt.get_rect(center=toast_rect.center))

    def _draw_initiative_spin(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        if not self.initiative_spin_active:
            return

        fog = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        fog.fill((18, 22, 30, 145))
        surface.blit(fog, (0, 0))

        center = (WIDTH // 2, HEIGHT // 2)
        wheel_size = 280
        wheel_radius = 120
        wheel = pygame.Surface((wheel_size, wheel_size), pygame.SRCALPHA)
        c = (wheel_size // 2, wheel_size // 2)

        # Two-sector wheel: top half 玩家先攻, bottom half AI先攻.
        pygame.draw.circle(wheel, (92, 134, 188), c, wheel_radius)
        pygame.draw.polygon(
            wheel,
            (70, 106, 156),
            [
                c,
                (c[0] - wheel_radius, c[1]),
                (c[0], c[1] + wheel_radius),
                (c[0] + wheel_radius, c[1]),
            ],
        )
        pygame.draw.circle(wheel, (190, 214, 240), c, wheel_radius, 3)
        pygame.draw.line(wheel, (190, 214, 240), (c[0] - wheel_radius, c[1]), (c[0] + wheel_radius, c[1]), 2)

        ptxt = fonts["btn"].render("玩家先攻", True, (242, 247, 252))
        atxt = fonts["btn"].render("AI先攻", True, (242, 247, 252))
        wheel.blit(ptxt, ptxt.get_rect(center=(c[0], c[1] - 46)))
        wheel.blit(atxt, atxt.get_rect(center=(c[0], c[1] + 46)))

        rotated = pygame.transform.rotozoom(wheel, -self.initiative_spin_current_angle, 1.0)
        surface.blit(rotated, rotated.get_rect(center=center))

        pointer = [(center[0], center[1] - 146), (center[0] - 12, center[1] - 124), (center[0] + 12, center[1] - 124)]
        pygame.draw.polygon(surface, (255, 228, 145), pointer)

        hint = fonts["small"].render("[系統] 轉盤決定先攻／後攻中...", True, (245, 236, 214))
        hint_rect = pygame.Rect(center[0] - 270, center[1] + 150, 540, 40)
        panel = pygame.Surface((hint_rect.width, hint_rect.height), pygame.SRCALPHA)
        draw_scroll_frame(
            panel,
            panel.get_rect(),
            (64, 50, 28, 200),
            (228, 192, 106, 220),
            (146, 116, 62, 210),
            (248, 220, 146, 220),
            radius=8,
        )
        surface.blit(panel, hint_rect.topleft)
        surface.blit(hint, hint.get_rect(center=hint_rect.center))

    def _spawn_firework(self) -> None:
        cx = random.randint(180, WIDTH - 180)
        cy = random.randint(120, HEIGHT // 2)
        palette = [
            (255, 218, 120),
            (255, 174, 104),
            (255, 244, 180),
            (255, 140, 98),
        ]
        for _ in range(26):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(2.2, 5.4)
            self.game_over_fireworks.append(
                {
                    "x": float(cx),
                    "y": float(cy),
                    "vx": math.cos(angle) * speed,
                    "vy": math.sin(angle) * speed,
                    "life": random.uniform(24.0, 40.0),
                    "max_life": random.uniform(24.0, 40.0),
                    "r": float(random.randint(2, 4)),
                    "cr": float(random.choice(palette)[0]),
                    "cg": float(random.choice(palette)[1]),
                    "cb": float(random.choice(palette)[2]),
                }
            )

    def _update_fireworks(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.firework_last_spawn_ms >= 380:
            self._spawn_firework()
            self.firework_last_spawn_ms = now

        alive_particles: List[Dict[str, float]] = []
        for p in self.game_over_fireworks:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.08
            p["vx"] *= 0.985
            p["life"] -= 1.0
            if p["life"] > 0:
                alive_particles.append(p)
        self.game_over_fireworks = alive_particles[-260:]

    def _draw_game_over_overlay(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        # Light blur over current battle frame to keep context while emphasizing result.
        small = pygame.transform.smoothscale(surface, (max(1, WIDTH // 6), max(1, HEIGHT // 6)))
        blurred = pygame.transform.smoothscale(small, (WIDTH, HEIGHT))
        surface.blit(blurred, (0, 0))

        veil = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        veil.fill((8, 12, 20, 120))
        surface.blit(veil, (0, 0))

        if self.game_over_victory:
            self._update_fireworks()
            for p in self.game_over_fireworks:
                fade = max(0.0, min(1.0, p["life"] / max(1.0, p["max_life"])))
                color = (int(p["cr"] * fade), int(p["cg"] * fade), int(p["cb"] * fade))
                pygame.draw.circle(surface, color, (int(p["x"]), int(p["y"])), int(p["r"]))

        center_x = WIDTH // 2
        title_y = HEIGHT // 2 - 120
        title_font = fonts["lobby_title"]

        if self.game_over_victory:
            txt = "勝利"
            shadow = title_font.render(txt, True, (58, 28, 8))
            burn = title_font.render(txt, True, (214, 132, 52))
            gold = title_font.render(txt, True, (255, 218, 130))
            surface.blit(shadow, shadow.get_rect(center=(center_x + 5, title_y + 7)))
            surface.blit(burn, burn.get_rect(center=(center_x + 2, title_y + 3)))
            surface.blit(gold, gold.get_rect(center=(center_x, title_y)))
        else:
            txt = "失敗"
            iron_shadow = title_font.render(txt, True, (40, 44, 52))
            iron = title_font.render(txt, True, (148, 154, 164))
            surface.blit(iron_shadow, iron_shadow.get_rect(center=(center_x + 4, title_y + 6)))
            iron_rect = iron.get_rect(center=(center_x, title_y))
            surface.blit(iron, iron_rect)
            for i in range(6):
                yoff = random.randint(-28, 28)
                x1 = iron_rect.left + random.randint(0, iron_rect.width // 2)
                x2 = x1 + random.randint(26, 90)
                y1 = iron_rect.centery + yoff
                y2 = y1 + random.randint(-10, 10)
                pygame.draw.line(surface, (86, 90, 98), (x1, y1), (x2, y2), 2)

        sub = fonts["h2"].render(self.game_over_text, True, (238, 228, 208))
        surface.blit(sub, sub.get_rect(center=(center_x, HEIGHT // 2 + 6)))

        self.btn_end_restart.rect = pygame.Rect(center_x - 248, HEIGHT // 2 + 68, 220, 56)
        self.btn_end_lobby.rect = pygame.Rect(center_x + 28, HEIGHT // 2 + 68, 220, 56)
        self.btn_end_restart.text = "重新開始"
        self.btn_end_lobby.text = "返回大廳"
        self.btn_end_restart.draw(surface, fonts["btn"])
        self.btn_end_lobby.draw(surface, fonts["btn"])

    def _schedule_ai_turn(self, attacker_name: str) -> None:
        self.ai_pending_active = True
        self.ai_pending_attacker = attacker_name
        base_delay = random.randint(2000, 4000)
        if self.difficulty == "普通":
            base_delay = int(base_delay * 0.9)
        elif self.difficulty == "困難":
            base_delay = int(base_delay * 0.75)
        self.ai_pending_delay_ms = max(500, base_delay)
        self.ai_pending_execute_ms = pygame.time.get_ticks() + self.ai_pending_delay_ms
        self.turn_info = "回合資訊：AI思考中..."
        self._append_log("【系統】AI 思考中...")

    def _ai_action_profile(self, attacker: Unit) -> Tuple[Card, str]:
        ally_targets = self._alive_by_factions(self._allied_factions(attacker.faction))
        enemy_targets = self._attackable_enemy_targets(attacker)
        attack_card = next((card for card in self.available_cards if card.card_type == "attack"), self.offensive_cards[0])
        ultimate_card = next((card for card in self.available_cards if card.card_type == "ultimate"), attack_card)
        defense_card = next((card for card in self.available_cards if card.card_type == "defense"), attack_card)
        heal_card = next((card for card in self.available_cards if card.card_type == "heal"), attack_card)
        heal_allowed = self._can_ai_use_heal(attacker, heal_card)

        if not ally_targets or not enemy_targets:
            if heal_allowed:
                return heal_card, attacker.name
            return defense_card, attacker.name

        hp_ratio = attacker.current_hp / max(1, attacker.hp)
        weakest_enemy = min(enemy_targets, key=lambda name: (self.units[name].current_hp, self.units[name].hp, name))
        low_hp_enemies = self._low_hp_enemy_targets(attacker, threshold=20)
        random_enemy = random.choice(enemy_targets)

        if self.difficulty == "簡單":
            if hp_ratio <= 0.45 and random.random() < 0.35:
                if hp_ratio <= 0.3 and random.random() < 0.45 and heal_allowed:
                    return heal_card, attacker.name
                return defense_card, attacker.name
            if random.random() < 0.12 and heal_allowed:
                return heal_card, attacker.name
            if low_hp_enemies and random.random() < 0.15:
                return ultimate_card, min(low_hp_enemies, key=lambda name: self.units[name].current_hp)
            return attack_card, random_enemy

        if self.difficulty == "普通":
            if hp_ratio <= 0.45 and random.random() < 0.78 and heal_allowed:
                return heal_card, attacker.name
            if hp_ratio <= 0.55 and random.random() < 0.35:
                return defense_card, attacker.name
            if low_hp_enemies and random.random() < 0.2:
                return ultimate_card, min(low_hp_enemies, key=lambda name: self.units[name].current_hp)
            return attack_card, weakest_enemy

        if hp_ratio <= 0.55 and random.random() < 0.85 and heal_allowed:
            return heal_card, attacker.name
        if hp_ratio <= 0.55 and random.random() < 0.3:
            return defense_card, attacker.name
        if low_hp_enemies:
            return ultimate_card, min(low_hp_enemies, key=lambda name: self.units[name].current_hp)
        return attack_card, weakest_enemy

    def _score_auto_player_candidate(self, unit: Unit) -> float:
        card, target_name = self._ai_action_profile(unit)
        hp_ratio = unit.current_hp / max(1, unit.hp)

        if card.card_type == "heal":
            return 220.0 + (1.0 - hp_ratio) * 120.0 + unit.spd * 0.2
        if card.card_type == "defense":
            return 180.0 + (1.0 - hp_ratio) * 100.0 + unit.def_ * 0.15

        target = self.units.get(target_name)
        projected_damage = 0
        if target is not None:
            projected_damage = self._calc_damage(unit, target, card)
        return projected_damage * 3.0 + unit.atk * 1.2 + unit.spd * 0.8 + hp_ratio * 25.0

    def _pick_auto_player_actor(self) -> Optional[Unit]:
        candidates = [unit for unit in self.units.values() if unit.alive and unit.faction in ["蜀", "吳"]]
        if not candidates:
            return None
        return max(candidates, key=lambda unit: (self._score_auto_player_candidate(unit), unit.spd, unit.atk, unit.name))

    def _execute_ai_turn(self, attacker_name: str) -> None:
        attacker = self.units.get(attacker_name)
        if attacker is None or not attacker.alive:
            return

        card, target_name = self._ai_action_profile(attacker)
        if not self._is_card_enabled_for_actor(attacker, card):
            card = next((c for c in self.available_cards if c.card_type == "attack"), self.offensive_cards[0])
            enemy_targets = self._attackable_enemy_targets(attacker)
            if enemy_targets:
                target_name = self._pick_ai_target(enemy_targets)
        if target_name not in self.units or not self.units[target_name].alive:
            target_name = attacker.name
        self.turn_info = f"回合資訊：AI 使用 {card.name}"
        self._apply_attack(attacker.name, target_name, card, from_ai=True)
        self.btn_attack.enabled = False
        self.btn_target_prev.enabled = False
        self.btn_target_next.enabled = False

    def _advance_turn_flow(self) -> None:
        if self._check_game_over():
            return

        while True:
            attacker_name = self._next_attacker()
            if attacker_name is None:
                return

            self.current_attacker = attacker_name
            attacker = self.units[attacker_name]
            self._clear_side_defense_modes(attacker.faction)

            if attacker.faction in ["蜀", "吳"]:
                if self.auto_mode:
                    self._current_auto_player_turn(attacker.name)
                    return
                self._enter_actor_selection_phase()
                return

            self.btn_attack.enabled = False
            self.btn_target_prev.enabled = False
            self.btn_target_next.enabled = False
            self._schedule_ai_turn(attacker.name)
            return

    def _advance_turn_to_factions(self, target_factions: List[str]) -> None:
        if self._check_game_over():
            return

        while True:
            attacker_name = self._next_attacker()
            if attacker_name is None:
                return

            self.current_attacker = attacker_name
            attacker = self.units[attacker_name]

            if attacker.faction not in target_factions:
                continue

            self._clear_side_defense_modes(attacker.faction)

            if attacker.faction in ["蜀", "吳"]:
                if self.auto_mode:
                    self._current_auto_player_turn(attacker.name)
                    return
                self._enter_actor_selection_phase()
                return

            self.btn_attack.enabled = False
            self.btn_target_prev.enabled = False
            self.btn_target_next.enabled = False
            self._schedule_ai_turn(attacker.name)
            return

    def _current_auto_player_turn(self, attacker_name: str) -> None:
        attacker = self._pick_auto_player_actor()
        if attacker is None or not attacker.alive:
            return

        self.current_attacker = attacker.name
        self.turn_info = f"回合資訊：自動操控 {attacker.name}"
        self._append_log(f"【系統】自動選擇 {attacker.name}")
        self._execute_ai_turn(attacker.name)
        if not self._check_game_over():
            self._advance_turn_to_factions(["魏"])

    def _update_ai_pending(self) -> None:
        if not self.ai_pending_active or not self.ai_pending_attacker:
            return
        if pygame.time.get_ticks() < self.ai_pending_execute_ms:
            return

        attacker_name = self.ai_pending_attacker
        self.ai_pending_active = False
        self.ai_pending_attacker = None
        self.ai_pending_execute_ms = 0
        self.ai_pending_delay_ms = 0

        if self._check_game_over():
            return
        self._execute_ai_turn(attacker_name)
        if not self._check_game_over():
            self._advance_turn_to_factions(["蜀", "吳"])

    def _enter_actor_selection_phase(self, show_prompt: bool = True) -> None:
        self.current_attacker = None
        self.card_selected = None
        self.targets = []
        self.target_index = -1
        self.awaiting_actor_selection = True
        self.awaiting_target_selection = False
        self.btn_attack.enabled = False
        self.btn_target_prev.enabled = False
        self.btn_target_next.enabled = False
        self.turn_info = "回合資訊：請先選擇要出戰的英雄"
        if show_prompt:
            self._show_toast("[系統] 請先選擇要出戰的英雄！")

    def _next_attacker(self) -> Optional[str]:
        if not self._alive_by_factions(["蜀", "吳"]) or not self._alive_by_factions(["魏"]):
            return None

        while True:
            if not self.turn_order or self.turn_index >= len(self.turn_order):
                self.turn_order = self._alive_sorted_names()
                self.turn_index = 0
                if not self.turn_order:
                    return None
            name = self.turn_order[self.turn_index]
            self.turn_index += 1
            if self.units[name].alive:
                return name

    def _check_game_over(self) -> bool:
        if self.game_over_active:
            return True

        player_side = self._alive_by_factions(["蜀", "吳"])
        enemy_side = self._alive_by_factions(["魏"])
        if player_side and enemy_side:
            return False

        self.btn_attack.enabled = False
        self.btn_target_prev.enabled = False
        self.btn_target_next.enabled = False
        self.auto_mode = False
        self.btn_auto.text = "開始自動攻擊"

        if player_side and not enemy_side:
            msg = "遊戲勝利！"
            self.game_over_victory = True
        else:
            msg = "遊戲失敗！"
            self.game_over_victory = False

        self.game_over_active = True
        self.game_over_text = msg
        self.firework_last_spawn_ms = pygame.time.get_ticks()
        self.game_over_fireworks = []

        self.turn_info = f"回合資訊：{msg}"
        self._append_log("=== 戰鬥結束 ===")
        self._append_log(msg)
        return True

    def _apply_attack(self, attacker_name: str, defender_name: str, card: Card, from_ai: bool = False) -> None:
        attacker = self.units[attacker_name]
        defender = self.units[defender_name]
        defender_was_alive = defender.alive
        used_heal_team_key: Optional[str] = None
        
        self._append_log(f"{attacker.name} 使用 {card.name}")

        if card.card_type == "heal" and attacker.current_hp >= attacker.hp:
            self._append_log(f"{attacker.name} 滿血，無法使用恢復")
            return
        if card.card_type == "heal" and self.heal_team_cooldowns.get(self._team_key(attacker.faction), 0) > 0:
            self._append_log(f"{attacker.name} 恢復仍在冷卻中")
            return
        if card.card_type == "ultimate" and defender.current_hp > 20:
            self._append_log("必殺技能只能對血量低於20的目標使用")
            return

        if card.card_type == "defense":
            attacker.defense_mode = True
            self._play_sfx("defense")
            self._append_log(f"{attacker.name} 進入防守狀態")
        elif card.card_type == "heal":
            heal = self._calc_heal(attacker, card)
            attacker.current_hp = min(attacker.hp, attacker.current_hp + heal)
            self.heal_team_cooldowns[self._team_key(attacker.faction)] = self.heal_cooldown_rounds
            used_heal_team_key = self._team_key(attacker.faction)
            self._play_sfx("heal")
            if from_ai:
                team_key = self._team_key(attacker.faction)
                self.ai_heal_uses_by_team[team_key] = self.ai_heal_uses_by_team.get(team_key, 0) + 1
            self._show_toast("恢復已使用，冷卻4輪！")
            self._append_log(f"{attacker.name} 恢復 {heal} HP")
        elif card.card_type == "ultimate":
            self._play_sfx("ultimate")
            defender.current_hp = 0
            self._append_log(f"{attacker.name} 對 {defender.name} 發動必殺，一擊擊破！")
        else:
            dmg = self._calc_damage(attacker, defender, card)
            defender.current_hp = max(0, defender.current_hp - dmg)
            if dmg > 0:
                self._play_sfx("hurt")
            self._create_damage_float(defender.name, dmg)
            self._append_log(f"{attacker.name} 對 {defender.name} 造成 {dmg} 傷害")

        if defender_name != attacker_name and defender_was_alive and not defender.alive:
            self._append_log(f"{defender.name} 已被擊敗")

        self._mark_valid_action_and_tick_round(attacker.faction, exclude_team_key=used_heal_team_key)

    def next_turn(self) -> None:
        self._advance_turn_flow()

    def player_attack(self) -> None:
        if not self.current_attacker or not self.card_selected:
            return
        attacker = self.units[self.current_attacker]
        if attacker.faction not in ["蜀", "吳"]:
            return
        
        card = self.card_selected
        if not self.targets or not (0 <= self.target_index < len(self.targets)):
            return
        target = self.targets[self.target_index]
        self._apply_attack(attacker.name, target, card)
        
        self.card_selected = None
        self.btn_attack.enabled = False
        self.btn_target_prev.enabled = False
        self.btn_target_next.enabled = False
        if not self._check_game_over():
            self._advance_turn_to_factions(["魏"])

    def toggle_auto(self) -> None:
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.btn_auto.text = "停止自動攻擊"
            self._append_log("【系統】自動攻擊已啟用")
            self._advance_turn_flow()
        else:
            self.btn_auto.text = "開始自動攻擊"
            self._append_log("【系統】自動攻擊已停止")
            self._show_toast_for_seconds("已切換手動操作", 2.0)
            locked = (
                self.start_countdown_active
                or self.initiative_spin_active
                or self.initiative_result_pending_active
                or self.ai_pending_active
            )
            # When auto mode is turned off during player side control, restore a clean manual-selection state.
            if not locked and self.current_attacker:
                unit = self.units.get(self.current_attacker)
                if unit is not None and unit.faction in ["蜀", "吳"]:
                    self._enter_actor_selection_phase(show_prompt=False)

    def draw_lobby(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        self.draw_background(surface, scene_type="lobby")

        card = pygame.Rect(170, 130, 840, 560)
        title_text = "赤壁之戰"
        title_pos = (card.centerx, card.y + 22)

        title_shadow = fonts["lobby_title"].render(title_text, True, (26, 13, 8))
        title_dark = fonts["lobby_title"].render(title_text, True, (120, 52, 20))
        title_burn = fonts["lobby_title"].render(title_text, True, (214, 102, 42))
        title_gold = fonts["lobby_title"].render(title_text, True, (255, 214, 142))

        title_shadow = pygame.transform.rotozoom(title_shadow, -1.8, 1.0)
        title_dark = pygame.transform.rotozoom(title_dark, -1.0, 1.0)
        title_burn = pygame.transform.rotozoom(title_burn, -0.6, 1.0)
        title_gold = pygame.transform.rotozoom(title_gold, 0.0, 1.0)

        surface.blit(title_shadow, title_shadow.get_rect(midtop=(title_pos[0] + 4, title_pos[1] + 6)))
        surface.blit(title_dark, title_dark.get_rect(midtop=(title_pos[0] + 2, title_pos[1] + 3)))
        surface.blit(title_burn, title_burn.get_rect(midtop=(title_pos[0], title_pos[1] + 2)))
        surface.blit(title_gold, title_gold.get_rect(midtop=title_pos))

        lines = [
            "歡迎來到赤壁之戰卡牌戰鬥！",
            "在這場戰役中，你將操控蜀國與吳國",
            "魏國實力非常之強大，請謹慎決定每一步！",
        ]
        y = card.y + 185
        for line in lines:
            shadow = fonts["body"].render(line, True, (16, 22, 30))
            shadow_rect = shadow.get_rect(midtop=(card.centerx + 1, y + 1))
            surface.blit(shadow, shadow_rect)
            txt = fonts["body"].render(line, True, DESC_TEXT)
            line_rect = txt.get_rect(midtop=(card.centerx, y))
            surface.blit(txt, line_rect)
            y += 42

        self.btn_start_game.draw(surface, fonts["btn"])
        self.btn_lobby_help.draw(surface, fonts["btn"])
        self.btn_lobby_quit.draw(surface, fonts["btn"])

        if self.lobby_help_active:
            self._draw_lobby_help_overlay(surface, fonts)

    def _draw_lobby_help_overlay(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        small = pygame.transform.smoothscale(surface, (max(1, WIDTH // 6), max(1, HEIGHT // 6)))
        blurred = pygame.transform.smoothscale(small, (WIDTH, HEIGHT))
        surface.blit(blurred, (0, 0))

        veil = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        veil.fill((10, 14, 22, 136))
        surface.blit(veil, (0, 0))

        box = pygame.Rect((WIDTH - 740) // 2, (HEIGHT - 370) // 2, 740, 370)
        panel = pygame.Surface((box.width, box.height), pygame.SRCALPHA)
        draw_scroll_frame(
            panel,
            panel.get_rect(),
            (26, 22, 16, 186),
            (214, 171, 86, 220),
            (148, 112, 56, 200),
            (248, 220, 146, 220),
            radius=14,
        )
        surface.blit(panel, box.topleft)

        title = fonts["h2"].render("遊戲說明", True, (246, 232, 196))
        surface.blit(title, title.get_rect(midtop=(box.centerx, box.y + 24)))

        body = (
            "本遊戲為三國題材回合制卡牌戰鬥。開局由轉盤決定先攻後攻，每回合都需選擇出戰角色與技能！\n"
            "技能介紹：攻擊：對敵方造成傷害，傷害計算會考慮攻擊力、防禦力\n"
            "防守：進入防守狀態，該局不可選中\n"
            "恢復：為自己恢復(10,20,30)HP(視難度而定)，冷卻時間4輪\n"
            "必殺：對血量低於20的敵人造成致命一擊\n"
            "攻擊、防守、恢復、必殺 各有妙用\n"
            "精準掌握節奏與技能才能擊破魏軍，完成赤壁決戰！"
        )
        self._draw_wrapped_text(
            surface,
            fonts["small"],
            body,
            (236, 226, 204),
            pygame.Rect(box.x + 36, box.y + 80, box.width - 72, 212),
            max_lines=7,
            line_spacing=6,
        )

        close_btn_rect = pygame.Rect(box.centerx - 90, box.bottom - 64, 180, 42)
        panel_btn = Button(close_btn_rect, "關閉")
        panel_btn.draw(surface, fonts["btn"])

    def draw_difficulty(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        self.draw_background(surface, scene_type="lobby")

        card = pygame.Rect(170, 130, 840, 560)
        self.draw_translucent_card(surface, card)

        h = fonts["h2"].render("難度選擇", True, DESC_TEXT)
        surface.blit(h, h.get_rect(midtop=(card.centerx, card.y + 26)))
        mouse_pos = pygame.mouse.get_pos()

        lines = [
            "請選擇難度！",
            "簡單會讓聯軍較有優勢，困難則讓魏軍更強",
        ]
        desc_box = pygame.Rect(card.x + 120, card.y + 88, card.width - 240, 86)
        rendered_lines = [fonts["small"].render(line, True, DESC_TEXT) for line in lines]
        gap = 8
        total_h = sum(txt.get_height() for txt in rendered_lines) + gap * (len(rendered_lines) - 1)
        y = desc_box.y + (desc_box.height - total_h) // 2
        for txt in rendered_lines:
            line_rect = txt.get_rect(center=(card.centerx, y + txt.get_height() // 2))
            surface.blit(txt, line_rect)
            y += txt.get_height() + gap

        # Keep both control rows horizontally centered in the difficulty card.
        top_y = card.y + 212
        top_gap = 64
        top_width = self.btn_diff_easy.rect.width
        top_total = top_width * 3 + top_gap * 2
        top_x = card.centerx - top_total // 2
        self.btn_diff_easy.rect = pygame.Rect(top_x, top_y, top_width, self.btn_diff_easy.rect.height)
        self.btn_diff_normal.rect = pygame.Rect(
            top_x + top_width + top_gap,
            top_y,
            top_width,
            self.btn_diff_normal.rect.height,
        )
        self.btn_diff_hard.rect = pygame.Rect(
            top_x + (top_width + top_gap) * 2,
            top_y,
            top_width,
            self.btn_diff_hard.rect.height,
        )

        bottom_y = card.y + 276
        bottom_gap = 28
        bottom_width = self.btn_toggle_battle_sfx.rect.width
        bottom_total = bottom_width * 2 + bottom_gap
        bottom_x = card.centerx - bottom_total // 2
        self.btn_toggle_battle_sfx.rect = pygame.Rect(
            bottom_x,
            bottom_y,
            bottom_width,
            self.btn_toggle_battle_sfx.rect.height,
        )
        self.btn_toggle_sound.rect = pygame.Rect(
            bottom_x + bottom_width + bottom_gap,
            bottom_y,
            bottom_width,
            self.btn_toggle_sound.rect.height,
        )

        # Action buttons row: keep centered and clearly separated from toggle row.
        self.btn_diff_continue.rect = pygame.Rect(card.centerx - 245, card.y + 410, 490, 56)
        self.btn_diff_back.rect = pygame.Rect(card.centerx - 245, card.y + 476, 490, 50)

        for label, btn in [
            ("簡單", self.btn_diff_easy),
            ("普通", self.btn_diff_normal),
            ("困難", self.btn_diff_hard),
        ]:
            selected = self.difficulty == label
            hovered = btn.rect.collidepoint(mouse_pos)
            if selected:
                bg = (244, 226, 164, 245) if hovered else (232, 208, 148, 236)
            else:
                bg = (84, 62, 30, 208) if hovered else (70, 52, 24, 188)
            draw_scroll_frame(
                surface,
                btn.rect,
                bg,
                (255, 244, 208) if selected else (226, 186, 96),
                (180, 146, 82) if selected else (126, 94, 48),
                (248, 220, 146),
                radius=8,
            )
            caption = fonts["btn"].render(label, True, (70, 44, 18) if selected else (252, 238, 204))
            surface.blit(caption, caption.get_rect(center=btn.rect.center))

        self.btn_toggle_battle_sfx.text = f"對局音效：{'開' if self.battle_sfx_enabled else '關'}"
        self.btn_toggle_sound.text = f"按鍵音效：{'開' if self.sound_enabled else '關'}"
        self.btn_toggle_battle_sfx.draw(surface, fonts["btn"])
        self.btn_toggle_sound.draw(surface, fonts["btn"])

        self.btn_diff_continue.draw(surface, fonts["btn"])
        self.btn_diff_back.text = "返回"
        self.btn_diff_back.draw(surface, fonts["btn"])

    def draw_name_entry(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        self.draw_background(surface, scene_type="lobby")

        card = pygame.Rect(170, 130, 840, 560)
        self.draw_translucent_card(surface, card)

        h = fonts["h2"].render("輸入玩家名稱", True, DESC_TEXT)
        surface.blit(h, h.get_rect(midtop=(card.centerx, card.y + 26)))

        hint_lines = [
            "請輸入暱稱，按Enter或開始遊戲即可進入戰場！",
            "如不需輸入將以 [ 主公 ] 開始遊戲！",
            "（注意：僅可輸入英文暱稱，及不得輸入敏感字詞！）",
        ]
        y = card.y + 92
        for line in hint_lines:
            txt = fonts["small"].render(line, True, DESC_TEXT)
            line_rect = txt.get_rect(midtop=(card.centerx, y))
            surface.blit(txt, line_rect)
            y += 30

        name_label = fonts["btn"].render("玩家名稱", True, DESC_TEXT)
        surface.blit(name_label, (card.x + 40, card.y + 248))
        self.name_entry_box = pygame.Rect(card.x + 40, card.y + 292, card.width - 80, 56)
        box_color = (236, 202, 120) if self.name_input_active else (214, 171, 86)
        draw_scroll_frame(
            surface,
            self.name_entry_box,
            (18, 16, 12),
            box_color,
            (128, 94, 44),
            (248, 220, 146),
            radius=8,
        )
        display_name = self.player_name if self.player_name else "請輸入你的名字（最多 12 字）"
        txt_color = (230, 236, 248) if self.player_name else (130, 148, 172)
        name_font = fonts["input"]
        name_txt = name_font.render(display_name, True, txt_color)
        name_rect = name_txt.get_rect(midleft=(self.name_entry_box.x + 16, self.name_entry_box.centery))
        surface.blit(name_txt, name_rect)
        if self.name_input_active:
            caret_x = name_rect.right + 4
            caret_y1 = self.name_entry_box.y + 12
            caret_y2 = self.name_entry_box.bottom - 12
            pygame.draw.line(surface, (235, 242, 252), (caret_x, caret_y1), (caret_x, caret_y2), 2)

        if self.name_error:
            err = fonts["small"].render(self.name_error, True, ERROR_TEXT)
            surface.blit(err, err.get_rect(midtop=(card.centerx, self.name_entry_box.bottom + 12)))

        self.btn_start_game.rect = pygame.Rect(card.x + 210, card.y + 390, 420, 56)
        self.btn_lobby_quit.rect = pygame.Rect(card.x + 210, card.y + 460, 420, 50)
        self.btn_start_game.text = "開始遊戲"
        self.btn_lobby_quit.text = "返回"
        self.btn_start_game.draw(surface, fonts["btn"])
        self.btn_lobby_quit.draw(surface, fonts["btn"])

    def draw_battle(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        self.draw_background(surface, dim_alpha=90, scene_type="battle")
        self._update_start_countdown()
        self._update_initiative_spin()
        self._update_initiative_result_pending()
        self._update_ai_pending()
        self._update_damage_floats(16.67)
        mouse_pos = pygame.mouse.get_pos()
        right_panel_rect = pygame.Rect(772, 124, 396, 624)
        draw_scroll_frame(
            surface,
            right_panel_rect,
            RIGHT_BG,
            (214, 171, 86),
            (154, 118, 58),
            (248, 220, 146),
            radius=8,
        )

        top_row_y = 22
        self.btn_lobby.rect = pygame.Rect(650, top_row_y, 130, 34)
        self.btn_restart.rect = pygame.Rect(790, top_row_y, 120, 34)
        self.btn_auto.rect = pygame.Rect(920, top_row_y, 120, 34)
        auto_start_ready = not (
            self.start_countdown_active
            or self.initiative_spin_active
            or self.initiative_result_pending_active
        )
        self.btn_auto.enabled = self.auto_mode or auto_start_ready

        self.btn_lobby.draw(surface, fonts["btn"])
        self.btn_restart.draw(surface, fonts["btn"])
        self.btn_auto.text = "停止自動攻擊" if self.auto_mode else "開始自動攻擊"
        self.btn_auto.draw(surface, fonts["btn"])
        self._draw_toast(surface, fonts)

        profile_text = f"玩家：{self.player_name}  難度：{self.difficulty}"
        ptxt = fonts["small"].render(profile_text, True, (190, 210, 234))
        surface.blit(ptxt, ptxt.get_rect(midleft=(20, self.btn_lobby.rect.centery)))
        self._draw_chibi_battlefield(surface, fonts)
        self._draw_damage_floats(surface, fonts)

        panel_x = 790
        panel_w = 350

        panel_frame = pygame.Surface((panel_w, 450), pygame.SRCALPHA)
        draw_scroll_frame(
            panel_frame,
            panel_frame.get_rect(),
            (241, 233, 214, 188),
            (214, 171, 86, 212),
            (154, 118, 58, 200),
            (248, 220, 146, 220),
            radius=8,
        )
        surface.blit(panel_frame, (panel_x, 140))

        control_title = fonts["h2_dark"].render("戰況控制台", True, TEXT_DARK)
        surface.blit(control_title, control_title.get_rect(midtop=(panel_x + panel_w // 2, 150)))

        info_box = pygame.Rect(panel_x + 8, 186, panel_w - 16, 128)
        draw_scroll_frame(
            surface,
            info_box,
            (248, 244, 232, 228),
            (214, 171, 86),
            (162, 126, 66),
            (248, 220, 146),
            radius=8,
        )
        self._draw_wrapped_text(
            surface,
            fonts["log"],
            self.turn_info,
            (22, 30, 40),
            pygame.Rect(info_box.x + 12, info_box.y + 10, info_box.width - 24, 38),
            max_lines=2,
            line_spacing=1,
        )

        pygame.draw.line(surface, (202, 164, 88), (info_box.x + 8, info_box.y + 58), (info_box.right - 8, info_box.y + 58), 1)
        target_label = fonts["log"].render("目前目標", True, (52, 64, 78))
        surface.blit(target_label, (info_box.x + 10, info_box.y + 64))
        actor_name = self.current_attacker if self.current_attacker else "未選擇"
        target_name = self.targets[self.target_index] if (0 <= self.target_index < len(self.targets)) else "未鎖定"
        actor_txt = fonts["log"].render(f"您的角色：{actor_name}", True, TEXT_DARK)
        target_txt = fonts["log"].render(f"攻擊目標：{target_name}", True, TEXT_DARK)
        surface.blit(actor_txt, (info_box.x + 10, info_box.y + 86))
        surface.blit(target_txt, (info_box.x + 10, info_box.y + 106))

        card_label = fonts["log"].render("選擇技能", True, (52, 64, 78))
        surface.blit(card_label, card_label.get_rect(midtop=(panel_x + panel_w // 2, 354)))
        card_y = 378
        self.card_buttons = []
        is_player_turn = bool(self.current_attacker) and self.units[self.current_attacker].faction in ["蜀", "吳"]

        if is_player_turn:
            offensive_w = (panel_w - 24) // 2
            offensive_h = 34
            offensive_y_step = 0
        else:
            offensive_w = panel_w - 16
            offensive_h = 44
            offensive_y_step = 52

        for i, card in enumerate(self.offensive_cards):
            card_rect = pygame.Rect(panel_x + 8, card_y + i * offensive_y_step, offensive_w, offensive_h)
            if is_player_turn:
                card_rect.x = panel_x + 8 + i * (offensive_w + 8)
            card_enabled = True
            if is_player_turn and self.current_attacker:
                card_enabled = self._is_card_enabled_for_actor(self.units[self.current_attacker], card)
            self.card_buttons.append((card_rect, card, card_enabled))
            is_selected = self.card_selected == card
            hovered = card_rect.collidepoint(mouse_pos)
            if not card_enabled:
                bg_color = (64, 56, 42, 178)
            elif is_selected:
                bg_color = (255, 247, 218, 252) if hovered else (246, 230, 176, 246)
            else:
                bg_color = (74, 52, 24, 224) if hovered else (54, 38, 18, 212)
            draw_scroll_frame(
                surface,
                card_rect,
                bg_color,
                (255, 248, 220) if is_selected else ((226, 186, 96) if card_enabled else (138, 122, 96)),
                (194, 160, 88) if is_selected else ((132, 98, 50) if card_enabled else (94, 84, 68)),
                (248, 220, 146),
                radius=6,
            )
            card_txt = fonts["log"].render(card.name, True, (74, 44, 16) if is_selected else (244, 228, 188))
            surface.blit(card_txt, card_txt.get_rect(center=card_rect.center))

        if is_player_turn:
            support_label = fonts["log"].render("恢復 / 防守", True, (52, 64, 78))
            surface.blit(support_label, (panel_x, 420))
            for i, card in enumerate(self.support_cards):
                card_rect = pygame.Rect(panel_x + 8 + i * (offensive_w + 8), 444, offensive_w, 34)
                card_enabled = self._is_card_enabled_for_actor(self.units[self.current_attacker], card)
                self.card_buttons.append((card_rect, card, card_enabled))
                is_selected = self.card_selected == card
                hovered = card_rect.collidepoint(mouse_pos)
                if not card_enabled:
                    bg_color = (64, 56, 42, 178)
                elif is_selected:
                    bg_color = (255, 247, 218, 252) if hovered else (246, 230, 176, 246)
                else:
                    bg_color = (74, 52, 24, 224) if hovered else (54, 38, 18, 212)
                draw_scroll_frame(
                    surface,
                    card_rect,
                    bg_color,
                    (255, 248, 220) if is_selected else ((226, 186, 96) if card_enabled else (138, 122, 96)),
                    (194, 160, 88) if is_selected else ((132, 98, 50) if card_enabled else (94, 84, 68)),
                    (248, 220, 146),
                    radius=6,
                )
                card_txt = fonts["log"].render(card.name, True, (74, 44, 16) if is_selected else (244, 228, 188))
                surface.blit(card_txt, card_txt.get_rect(center=card_rect.center))

            attacker_unit = self.units[self.current_attacker]
            ultimate_card = next((card for card in self.available_cards if card.card_type == "ultimate"), None)
            ultimate_ready = bool(ultimate_card and self._is_card_enabled_for_actor(attacker_unit, ultimate_card))
            if ultimate_ready and self.ultimate_ready_notified_actor != attacker_unit.name:
                self._show_toast("必殺技能可使用！")
                self.ultimate_ready_notified_actor = attacker_unit.name
            if not ultimate_ready and self.ultimate_ready_notified_actor == attacker_unit.name:
                self.ultimate_ready_notified_actor = None

        self.btn_attack.rect = pygame.Rect(panel_x, 536, panel_w, 42)
        self.btn_attack.text = "確認使用" if self.card_selected else "選擇卡牌"
        self.btn_attack.draw(surface, fonts["btn"])

        self.log_view_rect = pygame.Rect(panel_x, 590, panel_w, 140)
        draw_scroll_frame(
            surface,
            self.log_view_rect,
            (246, 242, 232),
            (214, 171, 86),
            (162, 126, 66),
            (248, 220, 146),
            radius=6,
        )
        max_offset = max(0, len(self.log_lines) - self.log_visible_lines)
        self.log_scroll_offset = min(self.log_scroll_offset, max_offset)
        end_idx = len(self.log_lines) - self.log_scroll_offset
        start_idx = max(0, end_idx - self.log_visible_lines)
        ylog = 602
        for line in self.log_lines[start_idx:end_idx]:
            t = fonts["log"].render(line, True, (35, 45, 58))
            surface.blit(t, (panel_x + 10, ylog))
            ylog += 15

        if self.opening_anim_timer > 0:
            ratio = self.opening_anim_timer / self.opening_anim_duration
            alpha = int(220 * ratio)
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((8, 12, 20, alpha))
            surface.blit(overlay, (0, 0))

            glow = int(220 + 35 * math.sin((1.0 - ratio) * math.pi * 8))
            start_text = fonts["title"].render("戰鬥開始", True, (255, glow, 140))
            surface.blit(start_text, start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            self.opening_anim_timer -= 1

        self._draw_initiative_spin(surface, fonts)
        if self.game_over_active:
            self._draw_game_over_overlay(surface, fonts)

    def draw(self, surface: pygame.Surface, fonts: Dict[str, pygame.font.Font]) -> None:
        if self.scene == "lobby":
            self.draw_lobby(surface, fonts)
        elif self.scene == "difficulty":
            self.draw_difficulty(surface, fonts)
        elif self.scene == "name_entry":
            self.draw_name_entry(surface, fonts)
        else:
            self.draw_battle(surface, fonts)

    def handle_click(self, pos: Tuple[int, int]) -> None:
        if self.scene == "lobby":
            if self.lobby_help_active:
                close_btn_rect = pygame.Rect((WIDTH - 740) // 2 + 740 // 2 - 90, (HEIGHT - 370) // 2 + 370 - 64, 180, 42)
                if close_btn_rect.collidepoint(pos):
                    self._play_sfx("click")
                    self.lobby_help_active = False
                    return
                # Clicking outside close button also closes the overlay for convenience.
                self._play_sfx("click")
                self.lobby_help_active = False
                return
            if self.btn_start_game.hit(pos):
                self._play_sfx("click")
                self.start_game()
                return
            if self.btn_lobby_help.hit(pos):
                self._play_sfx("click")
                self.lobby_help_active = True
                return
            if self.btn_lobby_quit.hit(pos):
                self._play_sfx("click")
                self.request_quit = True
                return
            return

        if self.scene == "difficulty":
            if self.btn_diff_easy.hit(pos):
                self.difficulty = "簡單"
                self._play_sfx("click")
                return
            if self.btn_diff_normal.hit(pos):
                self.difficulty = "普通"
                self._play_sfx("click")
                return
            if self.btn_diff_hard.hit(pos):
                self.difficulty = "困難"
                self._play_sfx("click")
                return
            if self.btn_toggle_battle_sfx.hit(pos):
                self.battle_sfx_enabled = not self.battle_sfx_enabled
                self._play_sfx("click")
                return
            if self.btn_toggle_sound.hit(pos):
                self.sound_enabled = not self.sound_enabled
                self._play_sfx("click")
                return
            if self.btn_diff_continue.hit(pos):
                self._play_sfx("click")
                self.start_name_entry()
                return
            if self.btn_diff_back.hit(pos):
                self._play_sfx("click")
                self.show_lobby()
                return
            return

        if self.scene == "name_entry":
            if self.name_entry_box.collidepoint(pos):
                self.name_input_active = True
                self.name_error = ""
                pygame.key.start_text_input()
                pygame.key.set_text_input_rect(self.name_entry_box)
                return
            if self.btn_start_game.hit(pos):
                self._play_sfx("click")
                self.confirm_name_and_start()
                return
            if self.btn_lobby_quit.hit(pos):
                self._play_sfx("click")
                pygame.key.stop_text_input()
                self.scene = "difficulty"
                self.name_input_active = False
                return
            return

        if self._is_startup_input_locked():
            return

        if self.game_over_active:
            if self.btn_end_restart.hit(pos):
                self._play_sfx("click")
                self._start_battle_with_initiative()
                return
            if self.btn_end_lobby.hit(pos):
                self._play_sfx("click")
                self.back_to_lobby()
                return
            return

        if self.btn_lobby.hit(pos):
            self._play_sfx("click")
            self.back_to_lobby()
            return
        if self.btn_restart.hit(pos):
            self._play_sfx("click")
            self._start_battle_with_initiative()
            return
        if self.btn_auto.rect.collidepoint(pos) and not self.btn_auto.enabled:
            self._show_toast_for_seconds("倒數結束後才能開始自動攻擊！", 2.0)
            return
        if self.btn_auto.hit(pos):
            self._play_sfx("click")
            self.toggle_auto()
            return
        if self.ai_pending_active:
            return
        # Directly click character cards to select player actor or lock target.
        if self.awaiting_actor_selection or (self.current_attacker and self.units[self.current_attacker].faction in ["蜀", "吳"]):
            for name, rect in self.unit_card_rects.items():
                if not rect.collidepoint(pos):
                    continue
                unit = self.units[name]
                if not unit.alive:
                    return
                if unit.faction in ["蜀", "吳"]:
                    self._play_sfx("click")
                    self.current_attacker = name
                    self.awaiting_actor_selection = False
                    self.awaiting_target_selection = True
                    self.card_selected = None
                    self.btn_attack.enabled = False
                    self._refresh_targets_for_current_selection()
                    self.turn_info = f"回合資訊：輪到 {name}，請選擇卡牌"
                    self._show_toast("[系統] 請選擇要攻擊的英雄！")
                    return
                if name in self.targets:
                    self._play_sfx("click")
                    self.target_index = self.targets.index(name)
                    self.awaiting_target_selection = False
                    return
        
        if hasattr(self, 'card_buttons'):
            if not self.current_attacker:
                return
            attacker = self.units.get(self.current_attacker)
            if attacker is None or attacker.faction not in ["蜀", "吳"]:
                return
            for card_rect, card, card_enabled in self.card_buttons:
                if card_rect.collidepoint(pos):
                    if not card_enabled:
                        if card.card_type == "ultimate":
                            self._show_toast_for_seconds("目前必殺不可用！", 2.0)
                        elif card.card_type == "heal":
                            cooldown_remain = self.heal_team_cooldowns.get(self._team_key(attacker.faction), 0)
                            if cooldown_remain > 0:
                                self._show_toast_for_seconds("恢復冷卻中！", 2.0)
                            elif attacker.current_hp >= attacker.hp:
                                self._show_toast_for_seconds("血量已滿！", 2.0)
                        return
                    self._play_sfx("click")
                    self.card_selected = card
                    self._refresh_targets_for_current_selection()
                    self.btn_attack.enabled = self.target_index != -1
                    return
        
        if self.btn_attack.hit(pos):
            self._play_sfx("click")
            self.player_attack()
            return

    def handle_key(self, event: pygame.event.Event) -> None:
        if self.scene != "name_entry" or not self.name_input_active:
            return
        if event.key == pygame.K_RETURN:
            self._play_sfx("click")
            self.confirm_name_and_start()
            return
        if event.key == pygame.K_BACKSPACE:
            self.player_name = self.player_name[:-1]
            self.name_error = ""

    def handle_text_input(self, text: str) -> None:
        if self.scene != "name_entry" or not self.name_input_active:
            return
        if len(self.player_name) < 12:
            remaining = 12 - len(self.player_name)
            self.player_name += text[:remaining]
            self.name_error = ""


def run(smoke_test: bool = False) -> None:
    pygame.init()
    mixer_ready = True
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=22050, size=-16, channels=1)
    except pygame.error:
        mixer_ready = False

    pygame.display.set_caption("赤壁之戰")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    def try_load_app_icon(path: Path) -> Optional[pygame.Surface]:
        if path.exists() and path.is_file():
            try:
                return pygame.image.load(str(path)).convert_alpha()
            except pygame.error:
                return None
        return None

    def make_tone(freq: int, duration_ms: int, volume: float = 0.35) -> Optional[pygame.mixer.Sound]:
        if not mixer_ready:
            return None
        sample_rate = 22050
        samples = int(sample_rate * duration_ms / 1000)
        wave = array("h")
        amplitude = int(32767 * volume)
        for i in range(samples):
            v = int(amplitude * math.sin(2.0 * math.pi * freq * (i / sample_rate)))
            wave.append(v)
        return pygame.mixer.Sound(buffer=wave.tobytes())

    def pick_font_name(candidates: List[str]) -> Optional[str]:
        for name in candidates:
            if pygame.font.match_font(name):
                return name
        return None

    cjk_font_name = pick_font_name(
        [
            "PingFang TC",
            "Heiti TC",
            "Hiragino Sans GB",
            "Noto Sans CJK TC",
            "Microsoft JhengHei",
            "Microsoft YaHei",
            "Arial Unicode MS",
            "Source Han Sans TC",
            "WenQuanYi Zen Hei",
        ]
    )
    calligraphy_font_name = pick_font_name(
        [
            "Kaiti TC",
            "STKaiti",
            "BiauKai",
            "DFKai-SB",
            "KaiTi",
            "Songti TC",
        ]
    ) or cjk_font_name
    mono_font_name = pick_font_name(["Menlo", "Monaco", "Courier New", "Consolas"]) or cjk_font_name

    def mkfont(name: Optional[str], size: int, bold: bool = False) -> pygame.font.Font:
        if name:
            return pygame.font.SysFont(name, size, bold=bold)
        return pygame.font.Font(None, size)

    fonts = {
        "title": mkfont(cjk_font_name, 30, bold=True),
        "lobby_title": mkfont(calligraphy_font_name, 128, bold=True),
        "h2": mkfont(cjk_font_name, 24, bold=True),
        "h2_dark": mkfont(cjk_font_name, 22, bold=True),
        "faction": mkfont(cjk_font_name, 20, bold=True),
        "body": mkfont(cjk_font_name, 20),
        "small": mkfont(cjk_font_name, 18),
        "input": mkfont(cjk_font_name, 26),
        "mono": mkfont(mono_font_name, 16),
        "btn": mkfont(cjk_font_name, 18, bold=True),
        "btn_dark": mkfont(cjk_font_name, 18),
        "log": mkfont(cjk_font_name, 16),
    }

    def try_load_background_image(path: Path) -> Optional[pygame.Surface]:
        if path.exists() and path.is_file():
            try:
                return pygame.image.load(str(path)).convert()
            except pygame.error:
                return None
        return None

    def try_load_scene_backgrounds(solution_dir: Path) -> Tuple[Optional[pygame.Surface], Optional[pygame.Surface]]:
        custom_dir = solution_dir / "遊戲圖片"
        lobby_bg: Optional[pygame.Surface] = None
        battle_bg: Optional[pygame.Surface] = None

        lobby_preferred = custom_dir / "背景.png"
        battle_preferred = custom_dir / "背景.png"
        lobby_bg = try_load_background_image(lobby_preferred)
        battle_bg = try_load_background_image(battle_preferred)

        if lobby_bg is None and custom_dir.exists() and custom_dir.is_dir():
            for path in sorted(custom_dir.iterdir()):
                if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                    lobby_bg = try_load_background_image(path)
                    if lobby_bg is not None:
                        break

        candidates = [
            solution_dir / "lobby_background.jpg",
            solution_dir / "lobby_background.png",
            solution_dir / "background.jpg",
            solution_dir / "background.png",
        ]
        if lobby_bg is None:
            for path in candidates:
                lobby_bg = try_load_background_image(path)
                if lobby_bg is not None:
                    break

        if battle_bg is None:
            battle_candidates = [
                solution_dir / "battle_background.jpg",
                solution_dir / "battle_background.png",
                solution_dir / "遊戲走道.png",
            ]
            for path in battle_candidates:
                battle_bg = try_load_background_image(path)
                if battle_bg is not None:
                    break

        if battle_bg is None:
            battle_bg = lobby_bg
        if lobby_bg is None:
            lobby_bg = battle_bg

        return lobby_bg, battle_bg

    app_icon = try_load_app_icon(Path(__file__).resolve().parent / "遊戲圖片" / "app圖示.png")
    if app_icon is not None:
        pygame.display.set_icon(app_icon)

    def resolve_data_file(candidates: List[str]) -> Path:
        current_dir = Path(__file__).resolve().parent
        search_roots = [current_dir, current_dir.parent, current_dir.parent.parent]
        for root in search_roots:
            for name in candidates:
                path = root / name
                if path.exists() and path.is_file():
                    return path
        return current_dir.parent / candidates[0]

    generals = resolve_data_file(["generals.txt", "角色資料主檔.txt"])
    game = ChibiBattlePygame(generals)
    lobby_bg_img, battle_bg_img = try_load_scene_backgrounds(Path(__file__).resolve().parent)
    game.set_background_images(lobby_bg_img, battle_bg_img)
    click_sfx = make_tone(740, 60)
    start_sfx = make_tone(520, 170)
    hurt_sfx = make_tone(180, 85, 0.30)
    heal_sfx = make_tone(920, 130, 0.24)
    defense_sfx = make_tone(320, 90, 0.26)
    ultimate_sfx = make_tone(110, 210, 0.34)
    game.set_sound_resources(
        mixer_ready,
        click_sfx,
        start_sfx,
        hurt_sfx,
        heal_sfx,
        defense_sfx,
        ultimate_sfx,
    )

    if smoke_test:
        game.draw(screen, fonts)
        pygame.display.flip()
        pygame.quit()
        return

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                game.handle_log_scroll(1)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                game.handle_log_scroll(-1)
            elif event.type == pygame.MOUSEWHEEL:
                game.handle_log_scroll(event.y)
            elif event.type == pygame.TEXTINPUT:
                game.handle_text_input(event.text)
            elif event.type == pygame.KEYDOWN:
                game.handle_key(event)

        if game.request_quit:
            running = False

        game.draw(screen, fonts)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke-test", action="store_true")
    args = parser.parse_args()
    run(smoke_test=args.smoke_test)


if __name__ == "__main__":
    main()