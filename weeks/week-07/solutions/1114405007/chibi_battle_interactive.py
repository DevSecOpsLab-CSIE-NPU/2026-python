# solution/chibi_battle_interactive.py
# 赤壁戰役 - 互動版 (可以真的玩！)
# 功能: 選擇武將 + 自選攻擊目標 + 回合制對戰 + 魏軍 AI 反擊

import os
import sys
import random
import time
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chibi_battle import ChibiBattle, General

GENERALS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'generals.txt'
)

# HP 進度條
def hp_bar(current, max_hp, width=12):
    filled = int(current / max_hp * width)
    filled = max(0, filled)
    bar = '█' * filled + '░' * (width - filled)
    color = ''
    if current / max_hp > 0.5:
        color = ''
    return f"{bar} {current:3}/{max_hp}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg="按 Enter 繼續..."):
    input(f"\n  {msg}")

def print_title():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║    吞食天地 - 赤壁戰役 │ 互動版  蜀吳聯軍 vs 曹操魏軍    ║")
    print("╚══════════════════════════════════════════════════════════╝")

# ─────────────────────────────────────────────
# 印出戰場狀態
# ─────────────────────────────────────────────
def print_battlefield(player_team, wei_team, current_hp, generals):
    print("\n" + "─" * 58)
    print("【我方陣營】")
    for i, name in enumerate(player_team, 1):
        g = generals[name]
        alive = "⚔" if current_hp[name] > 0 else "✝"
        bar = hp_bar(current_hp[name], g.hp)
        leader = " (軍師)" if g.is_leader else ""
        print(f"  {i}. {alive} {g.faction} {name:4} {bar}{leader}")

    print("【魏軍陣營】")
    for i, name in enumerate(wei_team, 1):
        g = generals[name]
        alive = "⚔" if current_hp[name] > 0 else "✝"
        bar = hp_bar(current_hp[name], g.hp)
        leader = " (軍師)" if g.is_leader else ""
        print(f"  {i}. {alive} {name:4} {bar}{leader}")
    print("─" * 58)

# ─────────────────────────────────────────────
# 選擇武將
# ─────────────────────────────────────────────
def choose_generals(generals):
    shu_wu = [g for g in generals.values() if g.faction in ('蜀', '吳')]
    shu_wu.sort(key=lambda g: g.spd, reverse=True)

    print("\n【選擇出戰武將】— 從蜀吳聯軍中選 3 位\n")
    for i, g in enumerate(shu_wu, 1):
        leader = " (軍師)" if g.is_leader else ""
        print(f"  {i}. [{g.faction}] {g.name:4}  攻{g.atk:2} 防{g.def_:2} 速{g.spd:2} HP{g.hp}{leader}")

    while True:
        try:
            raw = input("\n  輸入 3 個編號 (例如: 1 2 3): ").strip()
            choices = list(map(int, raw.split()))
            if len(choices) != 3:
                print("  ❌ 請選剛好 3 位武將")
                continue
            if len(set(choices)) != 3:
                print("  ❌ 不能重複選擇")
                continue
            if any(c < 1 or c > len(shu_wu) for c in choices):
                print(f"  ❌ 編號請在 1~{len(shu_wu)} 之間")
                continue
            return [shu_wu[c - 1].name for c in choices]
        except ValueError:
            print("  ❌ 請輸入數字，以空白分隔")

# ─────────────────────────────────────────────
# 玩家選攻擊者 & 目標
# ─────────────────────────────────────────────
def player_choose_attacker(player_team, current_hp, generals):
    alive = [n for n in player_team if current_hp[n] > 0]
    if not alive:
        return None
    print("\n  選擇攻擊者:")
    for i, name in enumerate(alive, 1):
        g = generals[name]
        print(f"    {i}. {g.faction} {name}  HP {current_hp[name]}/{g.hp}  攻{g.atk}")
    while True:
        try:
            c = int(input("  > ")) - 1
            if 0 <= c < len(alive):
                return alive[c]
            print(f"  ❌ 請輸入 1~{len(alive)}")
        except ValueError:
            print("  ❌ 請輸入數字")

def player_choose_target(wei_team, current_hp, generals):
    alive = [n for n in wei_team if current_hp[n] > 0]
    if not alive:
        return None
    print("  選擇攻擊目標:")
    for i, name in enumerate(alive, 1):
        g = generals[name]
        print(f"    {i}. {name}  HP {current_hp[name]}/{g.hp}  攻{g.atk} 防{g.def_}")
    while True:
        try:
            c = int(input("  > ")) - 1
            if 0 <= c < len(alive):
                return alive[c]
            print(f"  ❌ 請輸入 1~{len(alive)}")
        except ValueError:
            print("  ❌ 請輸入數字")

# ─────────────────────────────────────────────
# 攻擊計算
# ─────────────────────────────────────────────
def do_attack(attacker_name, defender_name, current_hp, generals, is_player=True):
    atk = generals[attacker_name]
    dfn = generals[defender_name]
    dmg = max(1, atk.atk - dfn.def_)
    current_hp[defender_name] = max(0, current_hp[defender_name] - dmg)

    side = "⚔️ 我方" if is_player else "💢 魏軍"
    print(f"\n  {side} {atk.faction if is_player else '魏'} {attacker_name}  →  攻擊  {defender_name}")
    print(f"       造成 {dmg} 傷害！  {defender_name} 剩餘 HP: {current_hp[defender_name]}/{generals[defender_name].hp}")

    if current_hp[defender_name] == 0:
        print(f"  💀 {defender_name} 陣亡！")

    return dmg

# ─────────────────────────────────────────────
# 魏軍 AI 反擊
# ─────────────────────────────────────────────
def wei_ai_attack(wei_team, player_team, current_hp, generals):
    alive_wei = [n for n in wei_team if current_hp[n] > 0]
    alive_player = [n for n in player_team if current_hp[n] > 0]
    if not alive_wei or not alive_player:
        return

    # AI: 選速度最快的存活魏將，攻擊防禦最低的我方
    attacker = max(alive_wei, key=lambda n: generals[n].spd)
    target = min(alive_player, key=lambda n: generals[n].def_)
    do_attack(attacker, target, current_hp, generals, is_player=False)

# ─────────────────────────────────────────────
# 主遊戲迴圈
# ─────────────────────────────────────────────
def run_interactive():
    # 讀取武將資料
    game = ChibiBattle()
    game.load_generals(GENERALS_FILE)
    generals = game.generals

    clear_screen()
    print_title()

    # --- 選擇出戰武將 ---
    player_team = choose_generals(generals)
    wei_team = [n for n in generals if generals[n].faction == '魏']

    # 初始化 HP
    current_hp = {name: g.hp for name, g in generals.items()}

    # --- 戰鬥開始 ---
    round_num = 0
    max_rounds = 9  # 最多 9 回合

    clear_screen()
    print_title()
    print(f"\n  我方出戰: {' ｜ '.join(player_team)}")
    print(f"  魏軍出陣: {' ｜ '.join(wei_team)}")
    pause("準備好後按 Enter 開戰！")

    while round_num < max_rounds:
        alive_player = [n for n in player_team if current_hp[n] > 0]
        alive_wei = [n for n in wei_team if current_hp[n] > 0]

        if not alive_player:
            break
        if not alive_wei:
            break

        round_num += 1
        clear_screen()
        print_title()
        print(f"\n  ══ 第 {round_num} 回合 ══")
        print_battlefield(player_team, wei_team, current_hp, generals)

        # 玩家攻擊
        attacker = player_choose_attacker(player_team, current_hp, generals)
        target = player_choose_target(wei_team, current_hp, generals)
        if attacker and target:
            do_attack(attacker, target, current_hp, generals, is_player=True)

        # 檢查魏全滅
        if not any(current_hp[n] > 0 for n in wei_team):
            break

        # 魏軍 AI 反擊
        print("\n  【魏軍反擊！】")
        wei_ai_attack(wei_team, player_team, current_hp, generals)

        # 檢查我方全滅
        if not any(current_hp[n] > 0 for n in player_team):
            break

        pause()

    # --- 結局 ---
    clear_screen()
    print_title()
    print_battlefield(player_team, wei_team, current_hp, generals)

    alive_player = [n for n in player_team if current_hp[n] > 0]
    alive_wei = [n for n in wei_team if current_hp[n] > 0]

    print()
    if alive_player and not alive_wei:
        print("  ╔══════════════════════════════════════╗")
        print("  ║  🎉 蜀吳聯軍大勝！赤壁之戰勝利！      ║")
        print("  ╚══════════════════════════════════════╝")
    elif alive_wei and not alive_player:
        print("  ╔══════════════════════════════════════╗")
        print("  ║  💀 蜀吳聯軍全滅，曹操笑到最後...    ║")
        print("  ╚══════════════════════════════════════╝")
    else:
        remaining_p = sum(current_hp[n] for n in player_team)
        remaining_w = sum(current_hp[n] for n in wei_team)
        if remaining_p >= remaining_w:
            print("  ╔══════════════════════════════════════╗")
            print("  ║  ⚔️  時間到！蜀吳剩餘兵力較多，判勝！  ║")
            print("  ╚══════════════════════════════════════╝")
        else:
            print("  ╔══════════════════════════════════════╗")
            print("  ║  ⚔️  時間到！魏軍剩餘兵力較多，判勝！  ║")
            print("  ╚══════════════════════════════════════╝")

    print(f"\n  共 {round_num} 回合結束。")
    print()


if __name__ == '__main__':
    run_interactive()
