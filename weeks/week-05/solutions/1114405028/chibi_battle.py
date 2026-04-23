# Chibi Battle Game - AI Generated Version
# This is the AI-taught version with Chinese comments

# 這是一個簡單的戰鬥遊戲實作
# 使用類別來表示戰士和戰鬥邏輯

class Warrior:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)
        return f"{self.name} attacks {enemy.name} for {self.attack} damage!"

def battle(warrior1, warrior2):
    round_num = 1
    while warrior1.is_alive() and warrior2.is_alive():
        print(f"Round {round_num}:")
        print(warrior1.attack_enemy(warrior2))
        if not warrior2.is_alive():
            break
        print(warrior2.attack_enemy(warrior1))
        round_num += 1
        print()

    if warrior1.is_alive():
        return f"{warrior1.name} wins!"
    else:
        return f"{warrior2.name} wins!"

# 使用範例
if __name__ == "__main__":
    hero = Warrior("Hero", 100, 20)
    monster = Warrior("Monster", 80, 15)
    result = battle(hero, monster)
    print(result)