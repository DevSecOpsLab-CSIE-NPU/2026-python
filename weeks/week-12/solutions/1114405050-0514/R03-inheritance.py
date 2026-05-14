# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# ── 基底類別 ─────────────────────────────────────────────
class Animal:
    # 這是基底類別（父類別），定義了所有動物共有的屬性與基礎行為
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # self.__class__.__name__ 可以動態取得目前的類別名稱，
        # 這樣繼承的子類別印出來就會是 Dog('...') 而不是 Animal('...')
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
# 在括號中填入父類別名稱即可完成繼承。Dog 繼承自 Animal，自動擁有其屬性與方法。
class Dog(Animal):
    # 方法覆寫 (Method Overriding)：子類別重新定義父類別中同名的方法，提供專屬的實作
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
class GuideDog(Dog):
    def __init__(self, name, owner):
        # super() 可以用來呼叫父類別的方法。
        # 這裡呼叫父類別的 __init__ 來設定 name，避免重複寫 self.name = name
        super().__init__(name)
        self.owner = owner

    def speak(self):
        # 透過 super().speak() 取得父類別 (Dog) 處理好的字串，再疊加額外的資訊
        base = super().speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
# isinstance 用於檢查「物件」是否屬於某個類別（或其父類別）
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

# issubclass 用於檢查「類別」是否為另一個類別的子類別
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# ── 多型（Polymorphism）──────────────────────────────────
def make_sounds(animals: list):
    # 這裡不需要用 if/else 判斷動物的類型，
    # 只要確保傳入的物件都有實作 speak() 方法，就會自動呼叫對應的行為，這就是「多型」的精髓。
    for a in animals:
        print(a.speak())

make_sounds([d, c, g])
