# R03. 繼承示範
# 這個範例展示類別繼承、方法覆寫、super() 呼叫，以及 isinstance / issubclass 的使用。

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    def speak(self):
        # 覆寫父類別的 speak 方法，輸出狗的叫聲
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


class GuideDog(Dog):
    def __init__(self, name, owner):
        # 使用 super() 呼叫父類別 Dog 的 __init__, 進而建立 Animal 的屬性
        super().__init__(name)
        self.owner = owner

    def speak(self):
        base = super().speak()  # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True，Dog 是 Animal 的子類別
print(isinstance(d, Cat))       # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False


def make_sounds(animals: list):
    for a in animals:
        print(a.speak())

make_sounds([d, c, g])
