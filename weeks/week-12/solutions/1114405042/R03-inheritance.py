"""
R03. 繼承與 super()（8.7）

本範例示範 Python 物件導向中最重要的概念之一：繼承。

重點包含：
    1. 基底類別（父類別）與子類別的關係
    2. 方法覆寫（override）如何改寫父類別行為
    3. super() 如何呼叫父類別的方法與初始化流程
    4. isinstance() 與 issubclass() 如何檢查物件與類別關係
    5. 多型：不同子類別可以提供不同的 speak() 行為

繼承的核心目的，是把共通行為放在父類別，讓子類別只補充差異部分。
"""

# ── 基底類別 ─────────────────────────────────────────────
class Animal:
    def __init__(self, name):
        # 父類別負責定義所有動物都共有的屬性。
        # 這裡 name 是每個動物都會有的基本資訊。
        self.name = name

    def speak(self):
        # 父類別提供一個預設行為。
        # 子類別可以覆寫這個方法，讓不同動物有不同的叫聲。
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # __class__.__name__ 會回傳目前物件所屬類別的名稱。
        # 這樣即使是子類別物件，也能正確顯示自己的類別名稱。
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
class Dog(Animal):
    # Dog 繼承 Animal，因此會自動擁有 Animal.__init__ 與 __repr__。
    # 這裡只覆寫 speak()，把預設的「發出聲音」改成狗的叫聲。
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    # Cat 也是 Animal 的子類別，但牠有自己的叫聲實作。
    def speak(self):
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
class GuideDog(Dog):
    # 導盲犬是狗的一種，所以先繼承 Dog，再額外加入 owner（主人）資訊。
    def __init__(self, name, owner):
        # super().__init__(name) 會沿著 MRO（方法解析順序）往上找初始化方法。
        # 因為 Dog 沒有自己定義 __init__，所以最後會呼叫到 Animal.__init__。
        # 這樣可以重用父類別的初始化邏輯，避免重複寫 self.name = name。
        super().__init__(name)      # 呼叫 Dog → Animal 的 __init__
        self.owner = owner

    def speak(self):
        # 先呼叫父類別的 speak()，取得狗原本的叫聲描述。
        # 這種寫法適合在保留父類別行為的同時，再加上子類別自己的額外資訊。
        base = super().speak()      # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立三個不同類別的物件。
# 雖然它們都是 Animal 家族成員，但行為可以因子類別而不同。
d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

# 這裡直接呼叫 speak()，可以看到每個類別各自的輸出內容不同。
# 這正是多型（polymorphism）的體現：同一個方法名稱，不同物件有不同反應。
for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
# isinstance(obj, Class) 用來檢查「某個物件是不是某個類別的實例」。
# 如果是子類別的實例，也會回傳 True，因為它本質上仍屬於父類別體系。
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

# issubclass(SubClass, BaseClass) 用來檢查「某個類別是不是另一個類別的子類別」。
# 這比 isinstance() 更偏向類別層級的關係判斷。
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# ── 多型（Polymorphism）──────────────────────────────────
def make_sounds(animals: list):
    # 這個函式不關心傳進來的是 Dog、Cat 還是 GuideDog。
    # 它只要求每個物件都要有 speak() 方法。
    # 這就是 Python 常見的「鴨子型別」風格：只要像鴨子、會叫，就當成鴨子。
    for a in animals:
        # 呼叫的是各自物件的 speak()，所以不同類別會表現出不同的行為。
        print(a.speak())        # 各自呼叫自己的 speak()

# 把不同類別的物件放進同一個清單中，交給同一個函式處理。
# 這個例子展示了多型：同一段程式可以處理不同型別的物件。
make_sounds([d, c, g])
