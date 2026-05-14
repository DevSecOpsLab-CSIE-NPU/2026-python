# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# 這份示範重點：
# 1) 繼承如何讓子類別重用父類別的屬性與方法
# 2) 方法覆寫（override）如何改寫父類別行為
# 3) super() 如何呼叫父類別的初始化與方法
# 4) isinstance / issubclass 如何判斷物件與類別關係
# 5) 多型（polymorphism）如何讓同一介面對應不同實作

# ── 基底類別 ─────────────────────────────────────────────
# Animal 是基底類別（父類別），提供子類別共用的基本功能
class Animal:
    def __init__(self, name):
        # 所有動物都有名字，先在父類別統一處理
        self.name = name

    def speak(self):
        # 父類別預設行為：只描述「發出聲音」
        # 子類別可以覆寫成更具體的叫聲
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # 用類別名稱與名稱欄位組成可讀的表示字串
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
# Dog 繼承 Animal，因此會自動擁有 Animal 的 __init__、__repr__ 等功能
class Dog(Animal):
    def speak(self):
        # 覆寫父類別的 speak()，改成狗叫聲
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        # 覆寫父類別的 speak()，改成貓叫聲
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
# GuideDog 是 Dog 的子類別，也就是 Animal 的孫類別
class GuideDog(Dog):
    def __init__(self, name, owner):
        # super().__init__() 會往上一層尋找初始化方法
        # 這裡實際會呼叫 Dog 沒有覆寫的情況下所繼承到的 Animal.__init__
        super().__init__(name)      # 呼叫 Dog → Animal 的 __init__
        self.owner = owner

    def speak(self):
        # 先呼叫父類別的 speak() 取得基礎文字，再加上導盲犬資訊
        base = super().speak()      # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立不同類型的動物物件，觀察各自的 speak() 行為
d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

# 用同一段迴圈處理不同子類別物件，這就是多型的典型示範
for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
# isinstance 用來判斷「物件是不是某個類別或其子類別的實例」
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

# issubclass 用來判斷「類別是不是某個類別的子類別」
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# ── 多型（Polymorphism）──────────────────────────────────
def make_sounds(animals: list):
    # 只要物件有 speak() 方法，就可以被這個函式使用
    for a in animals:
        print(a.speak())        # 各自呼叫自己的 speak()

# 同一個函式接受不同類型的動物物件，呼叫結果卻能不同
make_sounds([d, c, g])
