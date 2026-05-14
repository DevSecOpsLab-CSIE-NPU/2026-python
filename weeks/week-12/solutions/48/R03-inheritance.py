# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# ── 基底類別 ─────────────────────────────────────────────
class Animal:
    def __init__(self, name):
        # 基底類別先保存每個動物的名字。
        self.name = name

    def speak(self):
        # 預設行為：回傳一段通用的描述。
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # 讓除錯時顯示出類別名稱與名稱屬性。
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
class Dog(Animal):
    def speak(self):
        # 子類別可以改寫父類別的方法，提供自己的版本。
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        # 不同子類別可以有不同的行為。
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
class GuideDog(Dog):
    def __init__(self, name, owner):
        # 先沿用父類別的初始化邏輯，再補上自己的屬性。
        super().__init__(name)      # 呼叫 Dog → Animal 的 __init__
        self.owner = owner

    def speak(self):
        # 先取用父類別行為，再加上導盲犬自己的補充資訊。
        base = super().speak()      # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

# 依照各自類別的 speak() 實作輸出不同結果。
for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
# isinstance 用來檢查物件是不是某個類別或其子類別的實例。
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

# issubclass 用來檢查類別之間的繼承關係。
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# ── 多型（Polymorphism）──────────────────────────────────
def make_sounds(animals: list):
    # 只要物件有 speak()，就可以被同一段程式處理。
    for a in animals:
        print(a.speak())        # 各自呼叫自己的 speak()

make_sounds([d, c, g])
