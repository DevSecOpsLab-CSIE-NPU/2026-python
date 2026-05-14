"""R03 繼承與 super 簡化版。"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"


class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def speak(self):
        return f"{super().speak()}（導盲犬，主人：{self.owner}）"


def make_sounds(animals):
    return [animal.speak() for animal in animals]


def main():
    animals = [Dog("小黑"), Cat("咪咪"), GuideDog("阿金", "王伯伯")]
    for sound in make_sounds(animals):
        print(sound)


if __name__ == "__main__":
    main()
