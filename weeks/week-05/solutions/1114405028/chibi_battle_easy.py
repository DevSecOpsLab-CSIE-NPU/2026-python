# Chibi Battle Game - Easy Version (Hand-typed)
# 簡單版本的戰鬥遊戲，手動輸入的程式碼

class Warrior:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)

def battle(w1, w2):
    while w1.is_alive() and w2.is_alive():
        w1.attack_enemy(w2)
        if not w2.is_alive():
            break
        w2.attack_enemy(w1)

    if w1.is_alive():
        return w1.name
    else:
        return w2.name

if __name__ == "__main__":
    hero = Warrior("Hero", 100, 20)
    monster = Warrior("Monster", 80, 15)
    winner = battle(hero, monster)
    print(winner)