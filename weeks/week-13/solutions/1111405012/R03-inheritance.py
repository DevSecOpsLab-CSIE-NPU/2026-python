"""R03. 繼承與 super()（8.7）"""

from __future__ import annotations


class Animal:
    """所有動物的共同基底類別。"""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} 發出聲音"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    """覆寫 speak，讓狗有自己的叫聲。"""

    def speak(self) -> str:
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    """覆寫 speak，讓貓有自己的叫聲。"""

    def speak(self) -> str:
        return f"{self.name} 說：喵～"


class GuideDog(Dog):
    """導盲犬繼承狗，再加上主人資訊。"""

    def __init__(self, name: str, owner: str):
        super().__init__(name)
        self.owner = owner

    def speak(self) -> str:
        base_message = super().speak()
        return f"{base_message}（導盲犬，主人：{self.owner}）"


def make_sounds(animals: list[Animal]) -> list[str]:
    """示範多型：不同物件都能回應同一個 speak 介面。"""
    return [animal.speak() for animal in animals]


def main() -> None:
    """印出課堂上示範的繼承與多型結果。"""
    dog = Dog("小黑")
    cat = Cat("咪咪")
    guide_dog = GuideDog("阿金", "王伯伯")
    animals = [dog, cat, guide_dog]

    for sound in make_sounds(animals):
        print(sound)

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(isinstance(dog, Cat))
    print(issubclass(Dog, Animal))
    print(issubclass(Cat, Dog))

    for sound in make_sounds(animals):
        print(sound)


if __name__ == "__main__":
    main()
