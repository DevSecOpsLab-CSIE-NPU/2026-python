import sys

# 赤壁戰役模擬器 - 大一基礎版
# 這個版本使用最簡單的 list 和 dict，讓大家看懂檔案怎麼讀、資料怎麼算

def main():
    generals = [] # 儲存所有武將資訊

    # 1. 讀取武將資料 (Week 07 檔案讀取)
    try:
        with open('generals.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue

                # 分割字串： faction, name, hp, atk, def, spd, is_leader
                parts = line.split()
                # 把字串轉成對應的型態
                g = {
                    'faction': parts[0],
                    'name': parts[1],
                    'hp': int(parts[2]),
                    'atk': int(parts[3]),
                    'def': int(parts[4]),
                    'spd': int(parts[5]),
                    'is_leader': parts[6] == 'True'
                }
                generals.append(g)
    except FileNotFoundError:
        print("找不到 generals.txt 檔案！")
        return

    # 2. 戰鬥模擬 (Week 02 排序與計算)
    # 按速度排序 (由高到低)
    generals.sort(key=lambda x: x['spd'], reverse=True)

    damage_stats = {} # 記錄每個人造成的傷害
    loss_stats = {}   # 記錄每個人受到的傷害

    # 簡單模擬一波：蜀軍、吳軍打魏軍
    for g in generals:
        damage_stats[g['name']] = 0
        loss_stats[g['name']] = 0

    for attacker in generals:
        if attacker['faction'] in ['蜀', '吳']:
            # 隨便找一個魏軍當目標
            for target in generals:
                if target['faction'] == '魏':
                    # 傷害 = 攻擊 - 防禦 (最低 1)
                    dmg = attacker['atk'] - target['def']
                    if dmg < 1: dmg = 1

                    damage_stats[attacker['name']] += dmg
                    loss_stats[target['name']] += dmg
                    break # 打完一個人就換下一個武將

    # 3. 印出結果報告
    print("--- 赤壁戰役簡易報告 ---")
    for name, dmg in damage_stats.items():
        if dmg > 0:
            print(f"武將 {name} 造成了 {dmg} 點傷害")

if __name__ == "__main__":
    main()
