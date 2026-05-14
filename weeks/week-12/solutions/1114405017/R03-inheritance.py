# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# ── 基底類別 ─────────────────────────────────────────────
# 定義一個Animal基底類別，所有動物共有的基本特性
class Animal:
    # 建構函式：初始化動物名稱
    def __init__(self, name):
        self.name = name

    # speak方法：定義動物發出聲音的行為
    def speak(self):
        return f"{self.name} 發出聲音"

    # __repr__方法：定義物件的字串表示
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
# Dog類別繼承自Animal，並覆寫speak方法
class Dog(Animal):
    # 覆寫父類別的speak方法，提供狗特有的叫聲
    def speak(self):
        return f"{self.name} 說：汪汪！"


# Cat類別也繼承自Animal，並覆寫speak方法
class Cat(Animal):
    # 覆寫父類別的speak方法，提供貓特有的叫聲
    def speak(self):
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
# GuideDog類別繼承自Dog，並使用super()呼叫父類別方法
class GuideDog(Dog):
    # 建構函式：需要額外的owner參數
    def __init__(self, name, owner):
        super().__init__(name)      # 呼叫父類別Dog的__init__，再呼叫Animal的__init__
        self.owner = owner          # 初始化額外的實例變數

    # 覆寫speak方法，並呼叫父類別的speak方法
    def speak(self):
        base = super().speak()      # 呼叫父類別Dog的speak方法
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立不同動物的實例
d = Dog("小黑")      # 一般狗
c = Cat("咪咪")      # 貓
g = GuideDog("阿金", "王伯伯")  # 導盲犬

# 讓所有動物發出聲音
for animal in [d, c, g]:
    print(animal.speak())  # 每個動物呼叫自己的speak方法

# ── isinstance / issubclass ───────────────────────────────
# isinstance()：檢查物件是否為某類別的實例
print(isinstance(d, Dog))       # True：d是Dog類別的實例
print(isinstance(d, Animal))    # True：Dog是Animal的子類別，所以d也是Animal的實例
print(isinstance(d, Cat))       # False：d不是Cat類別的實例

# issubclass()：檢查一個類別是否為另一個類別的子類別
print(issubclass(Dog, Animal))  # True：Dog是Animal的子類別
print(issubclass(Cat, Dog))     # False：Cat不是Dog的子類別

# ── 多型（Polymorphism）──────────────────────────────────
# 多型：同一個方法在不同物件上有不同的行為
def make_sounds(animals: list):
    """讓所有動物發出聲音的函式"""
    for a in animals:
        print(a.speak())        # 呼叫每個動物的speak方法，行為因物件類型而異


# 示範多型：同一個make_sounds函式可以處理不同類型的動物
make_sounds([d, c, g])  # 狗、貓、導盲犬都會用自己的方式發出聲音
