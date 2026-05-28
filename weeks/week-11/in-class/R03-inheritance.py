# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# ── 基底類別 ─────────────────────────────────────────────
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)      # 呼叫 Dog → Animal 的 __init__
        self.owner = owner

    def speak(self):
        base = super().speak()      # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# ── 多型（Polymorphism）──────────────────────────────────
def make_sounds(animals: list):
    for a in animals:
        print(a.speak())        # 各自呼叫自己的 speak()

make_sounds([d, c, g])
