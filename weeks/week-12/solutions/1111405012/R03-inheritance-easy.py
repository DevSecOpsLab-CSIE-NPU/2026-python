"""R03 繼承與 super 詳細註解版。"""


class Animal:
    def __init__(self, name):
        # 所有動物都至少有名字，所以放在父類別。
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"


class Dog(Animal):
    # Dog 繼承 Animal，所以會自動擁有 name。
    # 這裡只要覆寫 speak 即可。
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


class GuideDog(Dog):
    def __init__(self, name, owner):
        # super() 會呼叫父類別的初始化，
        # 把 name 的設定沿用回來。
        super().__init__(name)
        self.owner = owner

    def speak(self):
        # 先拿到 Dog.speak() 的結果，再補充主人資訊。
        return f"{super().speak()}（導盲犬，主人：{self.owner}）"


def make_sounds(animals):
    # 多型的意思是：雖然物件型別不同，
    # 但只要都有 speak()，就能用同一種方式呼叫。
    return [animal.speak() for animal in animals]


def main():
    animals = [Dog("小黑"), Cat("咪咪"), GuideDog("阿金", "王伯伯")]
    for sound in make_sounds(animals):
        print(sound)


if __name__ == "__main__":
    main()
