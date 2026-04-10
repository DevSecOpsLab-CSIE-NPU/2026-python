# solution/chibi_battle_easy.py
# 三國武將 PK 版 - 赤壁戰役遊戲引擎 (AI 簡化版)
# 與 chibi_battle.py 功能相同，但邏輯更直觀易讀

from collections import namedtuple, Counter, defaultdict
import os

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])


def load_generals(filename):
    """讀取武將資料 (函式版，較易理解)"""
    generals = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == 'EOF':
                break
            if not line:
                continue
            parts = line.split()
            faction, name, hp, atk, def_, spd, is_leader = parts
            generals[name] = General(
                faction=faction,
                name=name,
                hp=int(hp),
                atk=int(atk),
                def_=int(def_),
                spd=int(spd),
                is_leader=(is_leader == 'True')
            )
    return generals


def simulate_battle(generals):
    """模擬三波戰鬥，回傳 damage Counter 和 losses defaultdict"""
    damage = Counter()
    losses = defaultdict(int)

    shu_wu = sorted(
        [g for g in generals.values() if g.faction in ('蜀', '吳')],
        key=lambda g: g.spd, reverse=True
    )
    wei = sorted(
        [g for g in generals.values() if g.faction == '魏'],
        key=lambda g: g.spd, reverse=True
    )

    for wave in range(1, 4):
        count = min(wave, len(shu_wu), len(wei))
        for i in range(count):
            a, d = shu_wu[i], wei[i]
            dmg_a = max(1, a.atk - d.def_)
            damage[a.name] += dmg_a
            losses[d.name] += dmg_a

            dmg_d = max(1, d.atk - a.def_)
            damage[d.name] += dmg_d
            losses[a.name] += dmg_d

    return damage, losses


def print_report(generals, damage, losses):
    """列印簡易報告"""
    print("\n【傷害排名 Top 5】")
    for i, (name, dmg) in enumerate(damage.most_common(5), 1):
        print(f"  {i}. {name} → {dmg} HP")

    print("\n【各勢力傷害總計】")
    faction_dmg = defaultdict(int)
    for name, dmg in damage.items():
        faction_dmg[generals[name].faction] += dmg
    for faction in ['蜀', '吳', '魏']:
        print(f"  {faction}: {faction_dmg.get(faction, 0)} HP")

    print("\n【戰敗將領】")
    defeated = [n for n, loss in losses.items() if loss >= generals[n].hp]
    print(f"  {defeated if defeated else '無'}")


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generals_path = os.path.join(base_dir, 'generals.txt')

    generals = load_generals(generals_path)
    damage, losses = simulate_battle(generals)
    print_report(generals, damage, losses)
